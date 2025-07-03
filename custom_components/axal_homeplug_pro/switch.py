from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
import tinytuya


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up switch platform."""
    device = tinytuya.OutletDevice(entry.data["id"], entry.data["ip"], entry.data["key"])
    async_add_entities([AXALChargerSwitch(device)], True)


class AXALChargerSwitch(SwitchEntity):
    """Switch to turn charging on/off."""

    def __init__(self, device):
        self._device = device
        self._attr_name = "AXAL Charger Power"
        self._attr_unique_id = f"{device.id}_switch"
        self._state = False

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        self._device.set_status(True, "switch")
        self._state = True

    def turn_off(self, **kwargs):
        self._device.set_status(False, "switch")
        self._state = False

    def update(self):
        status = self._device.status()
        self._state = status.get("switch", False)
