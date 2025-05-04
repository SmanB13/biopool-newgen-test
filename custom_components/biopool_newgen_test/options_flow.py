
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.config_entries import OptionsFlow
from .const import DOMAIN

OPTIONS_SCHEMA = vol.Schema({
    vol.Required("volume_m3", default=30): int,
    vol.Optional("cover_active", default=False): bool,
    vol.Optional("dashboard_enabled", default=True): bool,
    vol.Optional("pac_active", default=True): bool,
    vol.Optional("pac_consigne", default=26): int,
    vol.Optional("seuil_antigel", default=5): int,
    vol.Optional("temperature_entity", default=""): str,
    vol.Optional("pump_entity", default=""): str,
    vol.Optional("uv_entity", default=""): str,
    vol.Optional("oxybio_entity", default=""): str,
    vol.Optional("biobact_entity", default=""): str,
})

class OptionsFlowHandler(OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=self.add_suggested_values_to_schema(
                OPTIONS_SCHEMA, self.config_entry.options
            ),
        )
