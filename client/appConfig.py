
# Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))




import os
import sys
from gpiozero import PWMLED





gpioledODMainPwr = 23


# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"


# LEDGrowMainPWR = PWMLED(17)
# LEDGrowSup1PWR = PWMLED(27)
# LEDGrowSup2PWR = PWMLED(22)


# dimID = {
#     "LEDGrowMain": {"controller": LEDGrowMainPWR, "dimVal": 0},
#     "LEDGrowSup1": {"controller": LEDGrowSup1PWR, "dimVal": 0},
#     "LEDGrowSup2": {"controller": LEDGrowSup2PWR, "dimVal": 0},
# }


