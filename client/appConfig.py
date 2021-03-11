import os
import sys
# Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))





from gpiozero import PWMLED





gpioLedODMainPwr = 23
gpioLedPWMMainDim = 22
gpioLedPWMSupOneDim =17
gpioLedPWMSupTWoDim=27

# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"


# LEDGrowMainPWR = PWMLED(17)
# LEDGrowSup1PWR = PWMLED(27)
# LEDGrowSup2PWR = PWMLED(22)




