"""Tests for Ectocontrol api."""
import asyncio

import aiohttp

from custom_components.ectocontrol.api import (
    EctocontrolApiClient,
)
from custom_components.ectocontrol.core.model import EctoControlAPIDevices


async def main():
    async with aiohttp.ClientSession() as session:
        api = EctocontrolApiClient("05bd6f08a561b183f1eebc81800ad556da385b9c89f484fb9899f87261d6a67b", session)
        data: EctoControlAPIDevices = await api.async_get_devices()
        await api.async_get_data(data)

asyncio.run(main())
