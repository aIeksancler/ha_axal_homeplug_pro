from homeassistant.components.number import NumberEntity
from .const import DOMAIN
import tinytuya


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up number platform."""
    device = tinytuya.OutletDevice(entry.data["id"], entry.data["ip"], entry.data["key"])
    async_add_entities([AXALChargeCurrent(device)], True)


class AXALChargeCurrent(NumberEntity):
    """Number to set charging current."""

    def __init__(self, device):
        self._device = device
        self._attr_name = "AXAL Charge Current"
        self._attr_unique_id = f"{device.id}_charge_current"
        self._attr_min_value = 6
        self._attr_max_value = 32
        self._attr_step = 1
        self._value = 6

    @property
    def value(self):
        return self._value

    def set_value(self, value):
        self._device.set_status(int(value), "charge_cur_set")
        self._value = value

    def update(self):
        status = self._device.status()
        self._value = status.get("charge_cur_set", 6)
