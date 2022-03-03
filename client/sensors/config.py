from enum import Enum

import certifi


class SensorsTSLs(Enum):
    AIR_1 = 0
    AIR_2 = 1
    SOIL_1 = 2
    CO2_1 = 3
    VOC = 4


MONGO_CONFIGURATION = {
    "HOST": "mongodb+srv://subham:1234@cluster0.t4iwt.mongodb.net/testdb?retryWrites=true&w=majority",
    "tlsCAFile": certifi.where()}
