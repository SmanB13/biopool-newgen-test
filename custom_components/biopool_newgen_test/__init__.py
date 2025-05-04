import logging
_LOGGER = logging.getLogger(__name__)

DOMAIN = "biopool_newgen_test"

async def async_setup(hass, config):
    _LOGGER.info("✅ BioPool async_setup OK")
    return True

async def async_setup_entry(hass, entry):
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data | entry.options
    _LOGGER.info("✅ BioPool setup_entry OK, données : %s", entry.options)
    return True

async def async_unload_entry(hass, entry):
    hass.data[DOMAIN].pop(entry.entry_id, None)
    _LOGGER.info("♻️ BioPool unload_entry exécuté")
    return True



from homeassistant.core import callback
from homeassistant.config_entries import ConfigEntry


@staticmethod
@callback
def async_get_options_flow(config_entry: ConfigEntry):
    from .options_flow import OptionsFlowHandler
    return OptionsFlowHandler(config_entry)
