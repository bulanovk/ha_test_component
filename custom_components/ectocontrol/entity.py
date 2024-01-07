"""EctocontrolEntity class"""
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfTemperature
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import ATTRIBUTION
from .const import DOMAIN
from .const import NAME
from .const import VERSION
from .core.model import EctoControlAPIDevice


class EctocontrolEntity(CoordinatorEntity):
    device: EctoControlAPIDevice

    def __init__(self, coordinator, config_entry, device: EctoControlAPIDevice):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.device = device
        self._attr_name = self.device.name
        self._attr_unique_id = f"ec_{self.device.system_object_id}_{self.device.id}"
        if device.deviceClass == SensorDeviceClass.TEMPERATURE:
            self._attr_unique_id = f"{self._attr_unique_id}_temperature"
            _attr_device_class = SensorDeviceClass.TEMPERATURE
            _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
            _attr_state_class = SensorStateClass.MEASUREMENT

        self.entity_id = f"sensor.{self._attr_unique_id}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.device.system_object_id)},
            "name": f"{NAME}-{self.device.system_object_id}",
            "model": VERSION,
            "manufacturer": "Ectostroy",
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": str(self.coordinator.data.get("id")),
            "integration": DOMAIN,
        }
