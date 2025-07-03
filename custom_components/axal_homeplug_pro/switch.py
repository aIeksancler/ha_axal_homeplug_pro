from homeassistant.components.switch import SwitchEntity
from .const import DOMAIN, DEVICE_ID

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([ChargerSwitch(hass.data[DOMAIN])])

class ChargerSwitch(SwitchEntity):
    def __init__(self, device):
        self._device = device
        self._attr_name = "Charger Power"

    @property
    def is_on(self):
        return self._device.status.get("switch")

    async def async_turn_on(self, **kwargs):
        await self._device.set_property("switch", True)

    async def async_turn_off(self, **kwargs):
        await self._device.set_property("switch", False)
