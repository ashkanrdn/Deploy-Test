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
