from homeassistant.components.number import NumberEntity
from .const import DOMAIN, DEVICE_ID

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([ChargeCurrentEntity(hass.data[DOMAIN])])

class ChargeCurrentEntity(NumberEntity):
    def __init__(self, device):
        self._device = device
        self._attr_name = "Charge Current"
        self._attr_min_value = 6
        self._attr_max_value = 32
        self._attr_step = 1

    @property
    def value(self):
        return self._device.status.get("charge_cur_set")

    async def async_set_value(self, value):
        await self._device.set_property("charge_cur_set", int(value))
