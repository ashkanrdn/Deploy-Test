import os
import sys

# # Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
# print(os.path.dirname(__file__)+ "/amps")
# # import amps.lightingClass as amps

from amps.lightingClass import LedMain
from amps.testAshkan import hello


hello()



lighting= LedMain(17,22,27)
# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"


# LEDGrowMainPWR = PWMLED(17)
# LEDGrowSup1PWR = PWMLED(27)
# LEDGrowSup2PWR = PWMLED(22)

# amps.LedMain()
# dimID = {
#     "LEDGrowMain": {"controller": lighting.power, "dimVal": 0},
#     "LEDGrowSup1": {"controller": lighting.ledSuppOne, "dimVal": 0},
#     "LEDGrowSup2": {"controller": lighting.ledSuppTwo, "dimVal": 0},
# }