from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, DEVICE_ID

SENSORS = {
    "forward_energy_total": "Total Energy (kWh)",
    "power_total": "Power (kW)",
    "temp_current": "Temperature (°C)",
}

async def async_setup_entry(hass, config_entry, async_add_entities):
    device = hass.data[DOMAIN]
    entities = [ChargerSensor(device, key, name) for key, name in SENSORS.items()]
    async_add_entities(entities)

class ChargerSensor(SensorEntity):
    def __init__(self, device, key, name):
        self._device = device
        self._key = key
        self._attr_name = name

    @property
    def native_value(self):
        return self._device.status.get(self._key)
