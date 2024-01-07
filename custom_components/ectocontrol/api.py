"""Sample API Client."""
import asyncio
import logging
import socket

import aiohttp
import async_timeout

from custom_components.ectocontrol.core.model import EctoControlAPIDevices

TIMEOUT = 10

_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}
BASEURL = "https://my.ectostroy.ru/public_api/v0"


class EctocontrolApiClient:
    def __init__(
            self, public_token: str, session: aiohttp.ClientSession
    ) -> None:
        self._public_token = public_token
        HEADERS["Authorization"] = f"Bearer {public_token}"
        self._session = session

    async def async_get_devices(self) -> EctoControlAPIDevices:
        url = f"{BASEURL}/devices"
        try:
            _LOGGER.debug(f"Try to fetch URL={url}")
            maps = await self.api_wrapper("get", url, headers=HEADERS)
            _LOGGER.debug(f"GOT REST Result {maps}")
            return EctoControlAPIDevices(**maps)
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)
            return EctoControlAPIDevices(None)

    async def async_get_data(self, data: EctoControlAPIDevices) -> dict:
        _LOGGER.debug(f"API get Data Start {data.devices}")
        if not data.devices:
            _LOGGER.debug("No Devices to Update")
            return {"data": EctoControlAPIDevices(None)}
        url = f"{BASEURL}/info"
        ids = []
        for device in data.devices:
            ids.append(device.id)
        body = {"ids": ids}
        _LOGGER.debug(f"Try to fetch URL={url}, body={body}")
        res = await self.api_wrapper("post", url, data=body, headers=HEADERS)
        rez: dict[str, str] = {}
        for r in res.get("devices_info"):
            rez[r.get("id")] = r.get("value")
        return rez

    async def api_wrapper(
            self, method: str, url: str, data: dict = {}, headers: dict = {}
    ) -> dict:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(TIMEOUT):
                if method == "get":
                    response = await self._session.get(url, headers=headers)
                    return await response.json()

                elif method == "put":
                    await self._session.put(url, headers=headers, json=data)

                elif method == "patch":
                    await self._session.patch(url, headers=headers, json=data)

                elif method == "post":
                    response = await self._session.post(url, headers=headers, json=data)
                    return await response.json()

        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)
