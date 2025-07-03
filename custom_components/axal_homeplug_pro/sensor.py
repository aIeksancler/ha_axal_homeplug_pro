from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN
import tinytuya


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up sensor platform."""
    device = tinytuya.OutletDevice(entry.data["id"], entry.data["ip"], entry.data["key"])
    sensors = [
        AXALPowerSensor(device),
        AXALEnergySensor(device),
        AXALTemperatureSensor(device)
    ]
    async_add_entities(sensors, True)


class AXALPowerSensor(SensorEntity):
    """Sensor for current power draw."""

    def __init__(self, device):
        self._device = device
        self._attr_name = "AXAL Power Total"
        self._attr_unique_id = f"{device.id}_power"
        self._attr_unit_of_measurement = "kW"
        self._value = 0

    @property
    def native_value(self):
        return self._value

    def update(self):
        status = self._device.status()
        self._value = status.get("power_total", 0) / 1000  # convert W to kW


class AXALEnergySensor(SensorEntity):
    """Sensor for total energy."""

    def __init__(self, device):
        self._device = device
        self._attr_name = "AXAL Energy Total"
        self._attr_unique_id = f"{device.id}_energy"
        self._attr_unit_of_measurement = "kWh"
        self._value = 0

    @property
    def native_value(self):
        return self._value

    def update(self):
        status = self._device.status()
        self._value = status.get("forward_energy_total", 0) / 100  # scale


class AXALTemperatureSensor(SensorEntity):
    """Sensor for temperature."""

    def __init__(self, device):
        self._device = device
        self._attr_name = "AXAL Temperature"
        self._attr_unique_id = f"{device.id}_temp"
        self._attr_unit_of_measurement = "°C"
        self._value = 0

    @property
    def native_value(self):
        return self._value

    def update(self):
        status = self._device.status()
        self._value = status.get("temp_current", 0)
