"""Adds config flow for Blueprint."""
from __future__ import annotations

import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import selector

from custom_components.ectocontrol import DOMAIN
from custom_components.ectocontrol.const import *

_LOGGER = logging.getLogger(__name__)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Blueprint."""

    VERSION = 1

    async def async_step_user(
            self,
            user_input: dict | None = None,
    ) -> config_entries.FlowResult:
        """Handle a flow initialized by the user."""
        _errors = {}

        if user_input is not None:
            return self.async_create_entry(
                title="Stateful Scenes",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_SYSTEM_ID, default=DEFAULT_SCENE_PATH
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT)
                    ),
                    vol.Optional(
                        CONF_TOKEN, default=DEFAULT_NUMBER_TOLERANCE
                    ): selector.NumberSelector(
                        selector.NumberSelectorConfig(
                            min=TOLERANCE_MIN, max=TOLERANCE_MAX, step=TOLERANCE_STEP
                        )
                    ),
                    vol.Optional(
                        CONF_RESTORE_STATES_ON_DEACTIVATE,
                        default=DEFAULT_RESTORE_STATES_ON_DEACTIVATE,
                    ): selector.BooleanSelector(),
                    vol.Optional(
                        CONF_TRANSITION_TIME, default=DEFAULT_TRANSITION_TIME
                    ): selector.NumberSelector(
                        selector.NumberSelectorConfig(
                            min=TRANSITION_MIN, max=TRANSITION_MAX, step=TRANSITION_STEP
                        )
                    ),
                }
            ),
            errors=_errors,
        )

