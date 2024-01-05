"""Sensor platform for Ectocontrol."""
import logging

from . import EctocontrolDataUpdateCoordinator
from .const import DOMAIN
from .const import ICON
from .core.model import EctoControlAPIDevice
from .entity import EctocontrolEntity

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator: EctocontrolDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    _LOGGER.debug(f"Got Device List {coordinator.devices}")
    devs = []
    for device in coordinator.devices.devices:
        if device.type == "Датчик температуры":
            devs.append(EctocontrolSensor(coordinator, entry, device))
    async_add_devices(devs)


class EctocontrolSensor(EctocontrolEntity):
    """ectocontrol Sensor class."""

    def __init__(self, coordinator, config_entry, device: EctoControlAPIDevice):
        super().__init__(coordinator, config_entry, device)
        self.entity_id = f"sensor.ec_{self.device.system_object_id}_{self.device.id}"
        self._attr_unique_id = f"ec_{self.device.system_object_id}_{self.device.id}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("body")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "ectocontrol__custom_device_class"
