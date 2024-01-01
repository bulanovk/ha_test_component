from homeassistant import config_entries, data_entry_flow
from homeassistant.helpers.selector import selector
import voluptuous as vol
from custom_components.ectocontrol import DOMAIN


class ExampleConfigFlow(data_entry_flow.FlowHandler):
    async def async_step_user(self, user_input=None):
        return self.async_create_entry(
            title="Title of the entry",
            data={
                "username": user_input["username"],
                "password": user_input["password"]
            },
            options={
                "mobile_number": user_input["mobile_number"]
            },
        )