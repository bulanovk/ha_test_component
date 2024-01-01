import logging
from typing import Any, Dict, Optional

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant import config_entries, core
from homeassistant.const import CONF_ACCESS_TOKEN
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import *

_LOGGER = logging.getLogger(__name__)

AUTH_SCHEMA = vol.Schema(
    {vol.Required(CONF_ACCESS_TOKEN): cv.string}
)


async def validate_auth(access_token: str, hass: core.HomeAssistant) -> None:
    """Validates a GitHub access token.

    Raises a ValueError if the auth token is invalid.
    """
    session = async_get_clientsession(hass)


class EctocontrolConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Github Custom config flow."""

    data: Optional[Dict[str, Any]]

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        """Invoked when a user initiates a flow via the user interface."""
        errors: Dict[str, str] = {}
        if user_input is not None:
            try:
                await validate_auth(user_input[ATTR_PUBLIC_TOKEN], self.hass)
            except ValueError:
                errors["base"] = "auth"
            if not errors:
                # Input is valid, set data.
                self.data = user_input
                # Return the form of the next step.
                return self.async_create_entry(title="Ectocontrol", data=self.data)

        return self.async_show_form(
            step_id="system",
            data_schema=vol.Schema({vol.Required(ATTR_SYSTEM_ID): str,vol.Required(ATTR_PUBLIC_TOKEN): str})

        )
