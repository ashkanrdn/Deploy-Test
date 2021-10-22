import os
import sys
# Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from gpiozero import PWMLED




#\\\\\\\\\\\\\\\\\\\\\\ LED GPIO  //////////////////////

gpioLedDMainPwr = 18
gpioLedPWMMainDim = 25
gpioLedPWMSupOneDim = 13
gpioLedPWMSupTWoDim= 12


#\\\\\\\\\\\\\\\\\\\\\\ IRRIGATION GPIO  //////////////////////
# <<<< Supply >>>>
gpioIRGMainPump = 7
gpioIRGWtrSol = 22
gpioIRGNutrSol = 23
gpioIRGTankSwitchSol = 14


# <<<< Tank Sensors >>>>

# Main Supply Sensors
gpioIRGMainTankSensorFull = 20
gpioIRGMainTankSensorEmpty = 5
# Drain Supply Sensors
gpioIRGDrainTankSensorFull = 9
gpioIRGDrainTankSensorEmpty = 26

# <<<< Level Solonoids >>>>

gpioIRGlvl1Sol = 27
gpioIRGlvl2Sol = 17
gpioIRGlvl3Sol = 3
gpioIRGlvl4Sol = 15
gpioIRGlvl5Sol = 4

#\\\\\\\\\\\\\\\\\\\\\\ ARM  GPIO  //////////////////////

gpioARMEna = 10
gpioARMDir = 24
gpioARMPul = 21
gpioARMEndL = 8
gpioARMEndR = 11


#\\\\\\\\\\\\\\\\\\\\\\ AIR  GPIO  //////////////////////

gpioAIRMain = 19

# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"







