from typing import List, Dict


class Sensor:
    def __init__(self, sensor_tcl, name):
        self.sensor_tcl = sensor_tcl
        self.name = name

    def read_sensor(self):
        raise NotImplementedError


class AirSensor(Sensor):
    def read_sensor(self) -> Dict:
        temperature, relative_humidity = self.sensor_tcl.measurements
        return {"temperature": "%0.1f C" % temperature,
                "humidity": "%0.1f %%" % relative_humidity
                }


class SoilSensor(Sensor):
    def read_sensor(self):
        humidity = self.sensor_tcl.relative_humidity
        self.sensor_tcl.heater = True
        return {
            "humidity": "%0.1f %%" % humidity,
            "heater_status": self.sensor_tcl.heater
        }


class Co2Sensor(Sensor):
    def read_sensor(self):
        co2_in_ppm = self.sensor_tcl.CO2 if self.sensor_tcl.data_available else None
        return {"co2": co2_in_ppm}


class VoCSensor(Sensor):
    def __init__(self, tcl, name):
        Sensor.__init__(self, tcl, name)
        print("SGP30 serial #", [hex(i) for i in self.sensor_tcl.serial])
        self.sensor_tcl.iaq_init()
        self.sensor_tcl.set_iaq_baseline(0x8973, 0x8AAE)

    def read_sensor(self):
        estimated_co2 = self.sensor_tcl.eCO2
        tvoc = self.sensor_tcl.TVOC
        return {"estimated_co2": estimated_co2,
                "tvoc": tvoc
                }
