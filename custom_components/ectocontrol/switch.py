"""Switch platform for Ectocontrol."""
from typing import Any

from homeassistant.components.switch import SwitchEntity, _LOGGER

from .const import DOMAIN
from .entity import EctocontrolEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    _LOGGER.debug("Got Device List  %s", coordinator.devices)
    devs = []
    for device in coordinator.devices.devices:
        if device.type == "Реле электромагнитное":
            devs.append(EctocontrolBinarySwitch(coordinator, entry, device))
    async_add_devices(devs)


class EctocontrolBinarySwitch(EctocontrolEntity, SwitchEntity):  # pylint: disable=too-many-ancestors
    """ectocontrol switch class."""

    async def async_turn_on(self, **kwargs):  # pylint: disable=unused-argument
        """Turn on the switch."""
        await self.coordinator.api.async_set_title("bar")
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):  # pylint: disable=unused-argument
        """Turn off the switch."""
        await self.coordinator.api.async_set_title("foo")
        await self.coordinator.async_request_refresh()

    @property
    def is_on(self):
        """Return true if the switch is on."""
        _LOGGER.info("KOBU:SW:Stata - %s", self.coordinator.data.get(self.device.id))
        return self.coordinator.data.get(self.device.id) == "Вкл"

    def turn_off(self, **kwargs: Any) -> None:
        """Turn the entity off."""
        raise NotImplementedError()

    def turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        raise NotImplementedError()
