from enum import Enum



class LightingGPIOs:
    MAIN_POWER = 19
    # MAIN_DIM = 25
    # SUPP_ONE_DIM = 13
    # SUPP_TWO_DIM = 12


class IrrigationGPIOs:
    WATER_SOL = 17
    PRESS_RELIEF = 5
    NUTR_SOL = 27
    TANK_SWITCH = 14                                                             
    # TODO


class TankSensorGPIOs:
    MAIN_TANK_SENSOR_FULL = 20
    MAIN_TANK_SENSOR_EMPTY = 5
    # Drain Supply Sensors
    #DRAIN_TANK_SENSOR_FULL = 16
    #DRAIN_TANK_SENSOR_EMPTY = 26


class LevelSolenoidsGPIOs(Enum):
    LEVEL_1 = 22
    LEVEL_2 = 23
    LEVEL_3 = 24
    LEVEL_4 = 25


class ArmGPIOs:
    ENABLE = 10
    DIRECTION = 24
    PULSE = 21
    LEFT_LIMIT = 8
    RIGHT_LIMIT = 11


AIR_MAIN_GPIO = 26

DEFAULT_WATER_CYCLE_DURATION = 90
IRRIGATION_SCHEDULE = [
    ("01:30:00", DEFAULT_WATER_CYCLE_DURATION),

    ("09:30:00", DEFAULT_WATER_CYCLE_DURATION),
    ("17:30:00", DEFAULT_WATER_CYCLE_DURATION),
    
    ]
LIGHTING_SCHEDULE = [
    ("09:30:00", "17:30:00")
]
AIR_SCHEDULE = [
    ("07:00:00", "19:00:00")
]
