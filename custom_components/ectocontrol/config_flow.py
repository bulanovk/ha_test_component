from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN


class EctocontrolConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 1
    async def async_step_user(self, info):
        if info is not None:
            pass  # TODO: process info

        return self.async_show_form(
            step_id="token", data_schema=vol.Schema({vol.Required("token"): str})
        )

