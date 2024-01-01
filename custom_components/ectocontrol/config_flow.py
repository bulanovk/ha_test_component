from homeassistant import config_entries, data_entry_flow
from homeassistant.helpers.selector import selector
import voluptuous as vol
from custom_components.ectocontrol import DOMAIN


@config_entries.HANDLERS.register(DOMAIN)
class ExampleConfigFlow(data_entry_flow.FlowHandler):
    async def async_step_user(self, user_input=None):
        # Specify items in the order they are to be displayed in the UI
        data_schema = {
            vol.Required("username"): str,
            vol.Required("password"): str,
        }

        if self.show_advanced_options:
            data_schema["allow_groups"] = selector({
                "select": {
                    "options": ["all", "light", "switch"],
                }
            })

        return self.async_show_form(step_id="init", data_schema=vol.Schema(data_schema))