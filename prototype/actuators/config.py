from enum import Enum


class IrrigationGPIOs(Enum):
    MAIN_PUMP = 22
    LEVEL_ONE_SOL = 12


class LightGPIOs(Enum):
    MAIN_LED = 26


class FanGPIOs(Enum):
    FAN_ONE = 23
    FAN_TWO = 24
    FAN_THREE = 25


WATER_CYCLE_DURATION = 5

# Time format is "HH:MM:SS".
IRRIGATION_SCHEDULE = ["07:00:20", "11:00:20", "15:00:20", "19:00:20", "23:00:20"]
# [(time_on1, time_off1), (time_on2, time_off2)] make sure they do not overlap.
LIGHTING_SCHEDULE = [("06:59:20", "18:59:20")]
# [(time_on1, time_off1), (time_on2, time_off2)] make sure they do not overlap
AIR_SCHEDULE = [("06:59:20", "18:59:20")]
