"""Sensor platform for Ectocontrol."""
import logging

from . import EctocontrolDataUpdateCoordinator
from .const import DEFAULT_NAME
from .const import DOMAIN
from .const import ICON
from .const import SENSOR
from .core.model import EctoControlAPIDevices, EctoControlAPIDevice
from .entity import EctocontrolEntity

_LOGGER: logging.Logger = logging.getLogger(__package__)

async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator: EctocontrolDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    _LOGGER.debug("Going to read device List")
    devices: EctoControlAPIDevices = await coordinator.api.async_get_devices()
    _LOGGER.debug(f"Got Device List {devices}")
    for device in devices.devices:
        async_add_devices([EctocontrolSensor(coordinator, entry, device)])


class EctocontrolSensor(EctocontrolEntity):
    """ectocontrol Sensor class."""
    device: EctoControlAPIDevice

    def __init__(self, coordinator, config_entry, device: EctoControlAPIDevice):
        super().__init__(coordinator, config_entry)
        self.device = device

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.device.name

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
