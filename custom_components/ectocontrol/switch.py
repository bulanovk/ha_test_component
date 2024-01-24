"""Switch platform for Ectocontrol."""
from typing import Any

from homeassistant.components.switch import SwitchEntity, _LOGGER

from .const import DEFAULT_NAME
from .const import DOMAIN
from .const import ICON
from .const import SWITCH
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
    def name(self):
        """Return the name of the switch."""
        return f"{DEFAULT_NAME}_{SWITCH}"

    @property
    def icon(self):
        """Return the icon of this switch."""
        return ICON

    @property
    def is_on(self):
        """Return true if the switch is on."""
        return self.coordinator.data.get("title", "") == "foo"

    def turn_off(self, **kwargs: Any) -> None:
        """Turn the entity off."""
        raise NotImplementedError()

    def turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        raise NotImplementedError()
