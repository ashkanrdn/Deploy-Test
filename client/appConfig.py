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


gpioIRGMainPump = 14
gpioIRGWtrSol = 15
gpioIRGTankSwitchSol = 18
gpioIRGNutrSol = 23

gpioIRGlvl1Sol=24
gpioIRGlvl2Sol=4
gpioIRGlvl3Sol=8
gpioIRGlvl4Sol=3
gpioIRGlvl5Sol=17

gpioARMEna = 10
gpioARMDir = 24
gpioARMPul = 21
gpioARMEndL = 8
gpioARMEndR = 11


# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"


# LEDGrowMainPWR = PWMLED(17)
# LEDGrowSup1PWR = PWMLED(27)
# LEDGrowSup2PWR = PWMLED(22)




