from homeassistant.components.select import SelectEntity
from .const import DOMAIN, DEVICE_ID

MODES = ["charge_now", "charge_pct", "charge_energy", "charge_schedule"]

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([ChargeModeSelect(hass.data[DOMAIN])])

class ChargeModeSelect(SelectEntity):
    def __init__(self, device):
        self._device = device
        self._attr_name = "Charge Mode"
        self._attr_options = MODES

    @property
    def current_option(self):
        return self._device.status.get("work_mode")

    async def async_select_option(self, option):
        await self._device.set_property("work_mode", option)
