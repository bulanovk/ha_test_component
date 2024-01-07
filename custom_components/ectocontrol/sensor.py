"""Sensor platform for Ectocontrol."""
import logging
from datetime import date, datetime
from decimal import Decimal

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass, SensorEntity
from homeassistant.const import UnitOfTemperature
from homeassistant.helpers.typing import StateType

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
            devs.append(TemperatureEctoControlSensor(coordinator, entry, device))
    async_add_devices(devs)


class EctocontrolSensor(EctocontrolEntity, SensorEntity):
    """ectocontrol Sensor class."""

    def __init__(self, coordinator, config_entry, device: EctoControlAPIDevice):
        super().__init__(coordinator, config_entry, device)

    @property
    def native_value(self) -> StateType | date | datetime | Decimal:
        """Return the value reported by the sensor."""
        return self.coordinator.data.get(self.device.id)

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON


class TemperatureEctoControlSensor(EctocontrolSensor):

    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator, config_entry, device: EctoControlAPIDevice):
        super().__init__(coordinator, config_entry, device)
