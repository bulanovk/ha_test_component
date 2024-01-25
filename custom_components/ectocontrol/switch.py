"""Switch platform for Ectocontrol."""
from typing import Any

from homeassistant.components.switch import SwitchEntity, _LOGGER

from .core.const import SWITCH_TURN_ON_STATE, SWITCH_TURN_OFF_STATE
from .const import DOMAIN
from .entity import EctocontrolEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    _LOGGER.debug("Got Device List  %s", coordinator.devices)
    devs = []
    for key, device in coordinator.devices.devices.items():
        if device.type == "Реле электромагнитное":
            devs.append(EctocontrolBinarySwitch(coordinator, entry, device))
    async_add_devices(devs)


class EctocontrolBinarySwitch(EctocontrolEntity, SwitchEntity):  # pylint: disable=too-many-ancestors
    """ectocontrol switch class."""

    async def async_turn_on(self, **kwargs):  # pylint: disable=unused-argument
        """Turn on the switch."""
        self.device.state = SWITCH_TURN_ON_STATE
        await self.coordinator.api.async_set_state(self.device)
        # await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):  # pylint: disable=unused-argument
        """Turn off the switch."""
        self.device.state = SWITCH_TURN_OFF_STATE
        await self.coordinator.api.async_set_state(self.device)
        # await self.coordinator.async_request_refresh()

    @property
    def is_on(self):
        """Return true if the switch is on."""
        return self.coordinator.de.get(self.device.id) == SWITCH_TURN_ON_STATE

    def turn_off(self, **kwargs: Any) -> None:
        """Turn the entity off."""
        raise NotImplementedError()

    def turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        raise NotImplementedError()
