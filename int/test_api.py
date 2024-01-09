"""Tests for Ectocontrol api."""
import asyncio

import aiohttp

from custom_components.ectocontrol.api import (
    EctocontrolApiClient,
)
from custom_components.ectocontrol.core.model import EctoControlAPIDevices


async def main():
    """Test Function for API"""
    async with aiohttp.ClientSession() as session:
        api = EctocontrolApiClient("<TBD>", session)
        data: EctoControlAPIDevices = await api.async_get_devices()
        await api.async_get_data(data)


asyncio.run(main())
