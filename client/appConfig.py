import os
import sys
# Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))





from gpiozero import PWMLED





gpioLedODMainPwr = 20
gpioLedPWMMainDim = 21
gpioLedPWMSupOneDim =16
gpioLedPWMSupTWoDim=12
gpioMainPump = 14
gpioWtrPump=15
gpioTrnsPump=18
gpioNutrPump=23
gpiolvl1Sol=24
gpiolvl2Sol=25
gpiolvl3Sol=8
gpiolvl4Sol=7
gpiolvl5Sol=1

# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"


# LEDGrowMainPWR = PWMLED(17)
# LEDGrowSup1PWR = PWMLED(27)
# LEDGrowSup2PWR = PWMLED(22)




