import logging
from typing import Any, Dict, Optional

import voluptuous as vol
from homeassistant import config_entries
from homeassistant import data_entry_flow


from .const import *

_LOGGER = logging.getLogger(__name__)


@config_entries.HANDLERS.register(DOMAIN)
class EctocontrolConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Ectocontrol Custom config flow."""
    VERSION = 1

    data: Optional[Dict[str, Any]]

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        """Invoked when a user initiates a flow via the user interface."""
        if user_input is not None:
            self.data = user_input
            # Return the form of the next step.
            return self.async_create_entry(title="Ectocontrol", data=self.data)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required(ATTR_SYSTEM_ID): str, vol.Required(ATTR_PUBLIC_TOKEN): str})

        )
