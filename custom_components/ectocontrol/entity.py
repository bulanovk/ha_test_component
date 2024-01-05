"""EctocontrolEntity class"""
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

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.device.name

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"ec_{self.device.system_object_id}_{self.device.id}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": "Ectostroy",
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            # "id": str(self.coordinator.data.get("id")),
            "integration": DOMAIN,
        }
