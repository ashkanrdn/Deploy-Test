from enum import Enum


class LightingGPIOs:
    MAIN_POWER = 18
    MAIN_DIM = 25
    SUPP_ONE_DIM = 13
    SUPP_TWO_DIM = 12


class IrrigationGPIOs:
    MAIN_PUMP = 7
    WATER_SOL = 22
    NUTR_SOL = 23
    TANK_SWITCH = 14


class TankSensorGPIOs:
    MAIN_TANK_SENSOR_FULL = 20
    MAIN_TANK_SENSOR_EMPTY = 5
    # Drain Supply Sensors
    DRAIN_TANK_SENSOR_FULL = 16
    DRAIN_TANK_SENSOR_EMPTY = 26


class LevelSolenoidsGPIOs(Enum):
    LEVEL_1 = 27
    LEVEL_2 = 17
    LEVEL_3 = 3
    LEVEL_4 = 15
    LEVEL_5 = 4


class ArmGPIOs:
    ENABLE = 10
    DIRECTION = 24
    PULSE = 21
    LEFT_LIMIT = 8
    RIGHT_LIMIT = 11


AIR_MAIN_GPIO = 19

DEFAULT_WATER_CYCLE_DURATION = 15
IRRIGATION_SCHEDULE = [
    ("07:00:00", DEFAULT_WATER_CYCLE_DURATION),
                       ("11:00:00", DEFAULT_WATER_CYCLE_DURATION),
                       ("15:00:00", DEFAULT_WATER_CYCLE_DURATION),
                       ("19:00:00", DEFAULT_WATER_CYCLE_DURATION),
                       ("23:00:00", DEFAULT_WATER_CYCLE_DURATION)
                       ]
LIGHTING_SCHEDULE = [
    ("06:59:00", "18:59:00")
]
AIR_SCHEDULE = [
    ("07:00:00", "19:00:00")
]
