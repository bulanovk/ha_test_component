from homeassistant import core
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from custom_components.ectocontrol.const import DOMAIN


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Home Heat Calc component."""
    hass.data.setdefault(DOMAIN, {})

    return True
