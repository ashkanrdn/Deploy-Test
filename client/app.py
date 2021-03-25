import os
import sys
 # Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import socketio
import json
from gpiozero import LED
from time import sleep

#\\\\\\\\\\\\\\\\\\\\\\ AMPS IMPORTS //////////////////////

import appConfig as config
from amps.lightingClass import LedMain
from amps.Irrigation import Irrigation
from amps.Arm import ArmMaker
# # Config file variable
server_url = config.serverUrl  # connection server URL

#\\\\\\\\\\\\\\\\\\\\\\ GPIO ASSIGNMENTS //////////////////////

# LED CONTROLS

# gpioLedODMainPwr =  config.gpioLedODMainPwr
# gpioLedPWMMainDim =  config.gpioLedPWMMainDim
# gpioLedPWMSup1Dim = config.gpioLedPWMSupOneDim
# gpioLedPWMSup2Dim= config.gpioLedPWMSupTWoDim

# IRG CONTROLS

# gpioIRGMainPump =config.gpioIRGMainPump
# gpioIRGWtrSol=config.gpioIRGWtrSol
# gpioIRGNutrSol=config.gpioIRGNutrSol
# gpioIRGTankSwitchSol=config.gpioIRGTankSwitchSol

# gpioIRGlvl1Sol=config.gpioIRGlvl1Sol
# gpioIRGlvl2Sol=config.gpioIRGlvl2Sol
# gpioIRGlvl3Sol=config.gpioIRGlvl3Sol
# gpioIRGlvl4Sol=config.gpioIRGlvl4Sol
# gpioIRGlvl5Sol=config.gpioIRGlvl5Sol

#ARM CONTROLS

gpioARMEna = config.gpioARMEna
gpioARMDir = config.gpioARMDir
gpioARMPul = config.gpioARMPul
gpioARMEndL = config.gpioARMEndL
gpioARMEndR = config.gpioARMEndR

#\\\\\\\\\\\\\\\\\\\\\\ CONTROL CLASS INSTANTIATE //////////////////////

# lightingControls = LedMain(gpioPwr = gpioLedODMainPwr , gpioDim = gpioLedPWMMainDim , gpioSupp1 = gpioLedPWMSup1Dim, gpioSupp2 = gpioLedPWMSup2Dim)
#
# IRGControls =Irrigation(gpioIRGMainPump, gpioIRGWtrSol,gpioIRGTankSwitchSol, gpioIRGNutrSol,
#                 gpioIRGlvl1Sol, gpioIRGlvl2Sol, gpioIRGlvl3Sol, gpioIRGlvl4Sol, gpioIRGlvl5Sol)

ARMControls = ArmMaker(gpioARMEna,gpioARMDir,gpioARMPul,gpioARMEndL,gpioARMEndR)



#\\\\\\\\\\\\\\\\\\\\\\ SOCKET  //////////////////////

sio = socketio.Client()
sio.connect(server_url)

#\\\\\\\\\\\\\\\\\\\\\\ SOCKET CONNECTION   //////////////////////


@sio.event
def connect():
    print("I'm connected!")
    ARMControls.Callibrate()

#\\\\\\\\\\\\\\\\\\\\\\ SOCKET LED CONTROLS   //////////////////////


@sio.on("rangeChanged")
def rangeChanged(data):
    # a json containing controller ids and their values
    dashValues = json.loads(data)
    if dashValues['LEDGrowMainPwr'] == 1:
        lightingControls.on()
        mainDim =dashValues['LEDGrowMain']
        sup1Dim =dashValues['LEDGrowSup1']
        sup2Dim =dashValues['LEDGrowSup2']
        lightingControls.dim(mainDim,sup1Dim,sup2Dim)
    else:
        lightingControls.off()

#\\\\\\\\\\\\\\\\\\\\\\ IRRIGATION CONTROLS //////////////////////

# IRG PUMP CONTROLS
@sio.on("IRG")
def IRGChanged(data):
    dashValues = json.loads(data)
    for controlId in dashValues:
        IRGControl=getattr(IRGControls,controlId)
        if dashValues[controlId] == 1:
            IRGControl.on()
        else:
            IRGControl.off()

# IRG WATER CYCLE
@sio.on('IRGCycle')
def IRGCycleChanged(data):
    dashValues = json.loads(data)
        if( 'IRGWtrCycleTime' in dashValues ):
            IRGControls.waterCycle(int(dashValues['IRGWtrCycleTime']))
        else:
            IRGControls.waterCycle()

# IRG Nutrient Cycle
@sio.on('IRGCycleNutr')
def IRGCycleChangedNutr(data):
    dashValues = json.loads(data)
        if( 'IRGNutrCycleTime' in dashValues ):
            IRGControls.nutrientCycle(int(dashValues['IRGNutrCycleTime']))
        else:
            IRGControls.nutrientCycle()

#\\\\\\\\\\\\\\\\\\\\\\ ARM CONTROLS //////////////////////

stateStepperL =False
stateStepperR =False

# STEP TP L/R
@sio.on('Arm')
def ArmChanged(data):
    dashValues = json.loads(data)
    global stateStepperL
    global stateStepperR
    if('swingArmL' in dashValues):
        stateStepperL = dashValues['swingArmL']
    if('swingArmR' in dashValues):
        stateStepperR = dashValues['swingArmR']
globalLoc = 0

# ARM CALIBRATE
@sio.on('ArmCalibrated')
def ArmCalibrate(data):
    dashValues = json.loads(data)
    ARMControls.Callibrate()




# GO TO LOCATION
@sio.on('ArmLoc')
def ArmLocChanged(data):
    dashValues = json.loads(data)
    global globalLoc
    loc = int(dashValues['swingArmLoc'])
    globalLoc = loc
    ARMControls.goToLoc(loc)


while True:
    while stateStepperL == True:
        ARMControls.Pulsate('L')
    while stateStepperR == True:
        ARMControls.Pulsate('R')
