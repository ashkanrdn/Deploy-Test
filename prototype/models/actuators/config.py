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


WATER_CYCLE_DURATION = 15   

# Time format is "HH:MM:SS".
IRRIGATION_SCHEDULE = ["07:00:20",
                        "10:00:20",
                        # "12:57:00",
                        # "16:00:20", 
                        "21:00:20"]
# [(time_on1, time_off1), (time_on2, time_off2)] make sure they do not overlap.
LIGHTING_SCHEDULE = [("06:59:20", "10:40:00"),
                    ("11:10:00", "14:00:20"),
                    ("14:30:20", "15:40:20"),
                    ("16:10:20", "17:40:20"),
                    ("17:40:20", "18:40:20"),
                    ("19:10:20", "20:10:20"),
                    ("20:40:20", "21:40:20")]
# [(time_on1, time_off1), (time_on2, time_off2)] make sure they do not overlap
AIR_SCHEDULE = [("06:59:20", "23:59:20")]
