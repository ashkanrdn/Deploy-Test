from enum import Enum

import certifi


AIR_SENSORS_TSLS = {
    'AIR_1': 0,
    #  'AIR_2': 1
     }

SOIL_SENSORS_TSLS = {
    # 'SOIL_1': 2
    }

CO2_SENSORS_TSLS = {
    'CO2_1': 3
    }

VOC_SENSORS_TSLS = {
    'VOC_1': 4
    }

LIGHT_SENSOR_TSLS = {
    'LIGHT_1': 5
}

SLEEPING_TIME_IN_SECONDS = 3
# MONGO_CONFIGURATION = {
#     "HOST": "mongodb+srv://subham:1234@cluster0.t4iwt.mongodb.net/testdb?retryWrites=true&w=majority",
#     "tlsCAFile": certifi.where()}

SAMPLES_FILE_NAME = 'samples.csv'