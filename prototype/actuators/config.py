from enum import Enum

class IrrigationGPIOs(Enum):
    MainPump = 22
    Lvl1Sol = 12


class LightGPIOs(Enum): 
    LEDMain = 26

class FanGPIOs(Enum):
    FanOne = 23
    FanTwo = 24
    FanThree = 25