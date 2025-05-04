import voluptuous as vol
from homeassistant.config_entries import HANDLERS
from homeassistant import config_entries
from homeassistant.config_entries import HANDLERS
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig
from .const import DOMAIN

@HANDLERS.register(DOMAIN)
@HANDLERS.register(DOMAIN)
class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            return self.async_create_entry(title="BioPool NewGen", data=user_input, options=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("volume_m3", default=30): int,
                vol.Optional("cover_active", default=False): bool,
                vol.Optional("dashboard_enabled", default=True): bool,
                vol.Optional("pac_active", default=True): bool,
                vol.Optional("pac_consigne", default=26): int,
                vol.Optional("seuil_antigel", default=5): int,
                vol.Optional("temperature_entity"): EntitySelector(EntitySelectorConfig(domain="sensor")),
                vol.Optional("pump_entity"): EntitySelector(EntitySelectorConfig(domain="switch")),
                vol.Optional("uv_entity"): EntitySelector(EntitySelectorConfig(domain="switch")),
                vol.Optional("oxybio_entity"): EntitySelector(EntitySelectorConfig(domain="switch")),
                vol.Optional("biobact_entity"): EntitySelector(EntitySelectorConfig(domain="switch")),
            })
        )
