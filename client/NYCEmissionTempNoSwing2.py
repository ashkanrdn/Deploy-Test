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

#set watering time in seconds
waterDuration = 8

#times to water, turn on/off lights, turn on/off air in list format
waterTime = ["07:00:20", "11:00:20", "15:00:20", "19:00:20", "23:00:20"]
lightOn = ["06:59:20"]
lightOff = ["18:59:20"]
airOn = []
airOff = []

#operate the system at certain times per day
while True:
    dateSTR = datetime.datetime.now().strftime("%H:%M:%S")

    if dateSTR in airOn:
        print('Air on at',dateSTR)
        AIRControls.On()
        sleep(1)
    #ALWAYS USE DIM METHOD FOR TURNING LIGHTS ON AND OFF   
    elif dateSTR in lightOn:
        print('LED on at', dateSTR)
        LEDControls.dim()
        sleep(1)
    elif dateSTR in airOff:
        print('Air off at', dateSTR)
        AIRControls.Off()
        sleep(1)
    elif dateSTR in lightOff:
        print('LED off at', dateSTR)
        LEDControls.off()
        sleep(1)
    elif dateSTR in waterTime:
        print('Watering at', dateSTR)
        IRGControls.supplyTankCheck()
        IRGControls.waterCycle(cycleTime = waterDuration)
        sleep(1)
        IRGControls.IRGlvl1Sol.on()
        IRGControls.IRGlvl2Sol.on()
        sleep(10)
        IRGControls.IRGlvl1Sol.off()
        IRGControls.IRGlvl2Sol.off()
        sleep(1)
    else:
        sleep(1)
    
