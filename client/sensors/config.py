from enum import Enum
from sensor import *


class SensorsTypes(Enum):
    Air = AirSensor
    Soil = SoilSensor
    Co2 = Co2Sensor
    Light = LightSensor


TSLS = {
    SensorsTypes.Air: {},
    SensorsTypes.Soil: {},
    SensorsTypes.Co2: {},
    SensorsTypes.Light: {},
}

matrix_dimensions = {'levels': 1, 'elements': 1}


class SampleFileName(Enum):
    v1 = 'samples.csv'
