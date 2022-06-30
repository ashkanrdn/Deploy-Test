from logging import error
from amps.AIR import AIR
from amps.ARM import ARM
from amps.IRG import Irrigation as IRG
from amps.LED import LedMain as LED
import appConfig as config

from time import sleep
import json
import socketio
import os
import sys
import time
import datetime

# \\\\\\\\\\\\\\\\\\\\\\ GPIO ASSIGNMENTS //////////////////////

# LED CONTROLS

gpioLedDMainPwr = config.gpioLedDMainPwr
gpioLedPWMMainDim = config.gpioLedPWMMainDim
gpioLedPWMSup1Dim = config.gpioLedPWMSupOneDim
gpioLedPWMSup2Dim = config.gpioLedPWMSupTWoDim

# IRG CONTROLS

gpioIRGMainPump = config.gpioIRGMainPump
gpioIRGWtrSol = config.gpioIRGWtrSol
gpioIRGNutrSol = config.gpioIRGNutrSol
gpioIRGTankSwitchSol = config.gpioIRGTankSwitchSol

gpioIRGlvl1Sol = config.gpioIRGlvl1Sol
gpioIRGlvl2Sol = config.gpioIRGlvl2Sol
gpioIRGlvl3Sol = config.gpioIRGlvl3Sol
gpioIRGlvl4Sol = config.gpioIRGlvl4Sol
gpioIRGlvl5Sol = config.gpioIRGlvl5Sol

# Main Supply Sensors

gpioIRGMainTankSensorFull = config.gpioIRGMainTankSensorFull
gpioIRGMainTankSensorEmpty = config.gpioIRGMainTankSensorEmpty
# Drain Supply Sensors

gpioIRGDrainTankSensorFull = config.gpioIRGDrainTankSensorFull
gpioIRGDrainTankSensorEmpty = config.gpioIRGDrainTankSensorEmpty

# ARM CONTROLS

gpioARMEna = config.gpioARMEna
gpioARMDir = config.gpioARMDir
gpioARMPul = config.gpioARMPul
gpioARMEndL = config.gpioARMEndL
gpioARMEndR = config.gpioARMEndR

# AIR CONTROLS

gpioAIRMain = config.gpioAIRMain


# \\\\\\\\\\\\\\\\\\\\\\ CONTROL CLASS INSTANTIATE //////////////////////

LEDControls = LED(gpioLedDMainPwr, gpioLedPWMMainDim,gpioLedPWMSup1Dim, gpioLedPWMSup2Dim)

IRGControls = IRG(gpioIRGMainPump, gpioIRGWtrSol, gpioIRGTankSwitchSol, gpioIRGNutrSol,
                  gpioIRGlvl1Sol, gpioIRGlvl2Sol, gpioIRGlvl3Sol, gpioIRGlvl4Sol, gpioIRGlvl5Sol,
                  gpioIRGMainTankSensorFull, gpioIRGMainTankSensorEmpty, gpioIRGDrainTankSensorFull, gpioIRGDrainTankSensorEmpty
                  ,LEDObj = LEDControls)

ARMControls = ARM(gpioARMEna, gpioARMDir, gpioARMPul, gpioARMEndL, gpioARMEndR)


AIRControls = AIR(gpioAIRMain)

print('moving right, to intereupt press ctr+C')
while True:
   
    ARMControls.Pulsate(dir='R')
    #ARMControls.ARML2RTotalStps += 1
    #ARMControls.ARMLoc += 1
