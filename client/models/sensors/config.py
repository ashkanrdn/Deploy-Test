from enum import Enum

AIR_SENSORS_TSLS = {
    'AIR_INSIDE': 0,
    'AIR_OUTSIDE': 7
}

SOIL_SENSORS_TSLS = {
    'SOIL': 2
}

CO2_SENSORS_TSLS = {
    'CO2_INSIDE': 3,
    'CO2_OUTSIDE': 6
}

VOC_SENSORS_TSLS = {
    'VOC_INSIDE': 4,
    'VOC_OUTSIDE': 1
}

LIGHT_SENSOR_TSLS = {
    'LIGHT': 5
}

SLEEPING_TIME_IN_SECONDS = 3


class SampleFileName(Enum):
    v1 = 'samples.csv'
    v2 = 'samples/samples_v2.csv'
    v3 = 'samples/samples_v3.csv'
    v4 = 'samples/samples_v3.csv'
