import os
import sys
 # Modify PATH so we can import files from elsewhere in this direcotry
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import socketio
import json
from gpiozero import LED
from time import sleep

#\\\\\\\\\\\\\\\\\\\\\\ AMPS IMPORTS //////////////////////

import appConfig as config
from amps.LED import LedMain as LED
from amps.IRG import Irrigation as IRG
from amps.ARM import ARM
from amps.AIR import AIR


# # Config file variable
server_url = config.serverUrl  # connection server URL

#\\\\\\\\\\\\\\\\\\\\\\ GPIO ASSIGNMENTS //////////////////////

# LED CONTROLS

gpioLedDMainPwr =  config.gpioLedDMainPwr
gpioLedPWMMainDim =  config.gpioLedPWMMainDim
gpioLedPWMSup1Dim = config.gpioLedPWMSupOneDim
gpioLedPWMSup2Dim= config.gpioLedPWMSupTWoDim

# IRG CONTROLS

gpioIRGMainPump =config.gpioIRGMainPump
gpioIRGWtrSol=config.gpioIRGWtrSol
gpioIRGNutrSol=config.gpioIRGNutrSol
gpioIRGTankSwitchSol=config.gpioIRGTankSwitchSol

gpioIRGlvl1Sol=config.gpioIRGlvl1Sol
gpioIRGlvl2Sol=config.gpioIRGlvl2Sol
gpioIRGlvl3Sol=config.gpioIRGlvl3Sol
gpioIRGlvl4Sol=config.gpioIRGlvl4Sol
gpioIRGlvl5Sol=config.gpioIRGlvl5Sol

# Main Supply Sensors

gpioIRGMainTankSensorFull = config.gpioIRGMainTankSensorFull
gpioIRGMainTankSensorEmpty = config.gpioIRGMainTankSensorEmpty
# Drain Supply Sensors

gpioIRGDrainTankSensorFull = config.gpioIRGDrainTankSensorFull
gpioIRGDrainTankSensorEmpty = config.gpioIRGDrainTankSensorEmpty

#ARM CONTROLS

gpioARMEna = config.gpioARMEna
gpioARMDir = config.gpioARMDir
gpioARMPul = config.gpioARMPul
gpioARMEndL = config.gpioARMEndL
gpioARMEndR = config.gpioARMEndR

#AIR CONTROLS

gpioAIRMain=config.gpioAIRMain




#\\\\\\\\\\\\\\\\\\\\\\ CONTROL CLASS INSTANTIATE //////////////////////

LEDControls = LED(gpioLedDMainPwr, gpioLedPWMMainDim, gpioLedPWMSup1Dim, gpioLedPWMSup2Dim)

IRGControls =IRG(gpioIRGMainPump, gpioIRGWtrSol,gpioIRGTankSwitchSol, gpioIRGNutrSol,
                gpioIRGlvl1Sol, gpioIRGlvl2Sol, gpioIRGlvl3Sol, gpioIRGlvl4Sol, gpioIRGlvl5Sol,
                gpioIRGMainTankSensorFull,gpioIRGMainTankSensorEmpty,gpioIRGDrainTankSensorFull,gpioIRGDrainTankSensorEmpty
                )

ARMControls = ARM(gpioARMEna,gpioARMDir,gpioARMPul,gpioARMEndL,gpioARMEndR)


AIRControls = AIR(gpioAIRMain)
#\\\\\\\\\\\\\\\\\\\\\\ SOCKET INIT //////////////////////

sio = socketio.Client()
sio.connect(server_url)

#\\\\\\\\\\\\\\\\\\\\\\ SOCKET CONNECTION   //////////////////////


@sio.event
def connect():
    print("AMPS Conntected to Control Dashboard!")
    # ARMControls.Callibrate()



#\\\\\\\\\\\\\\\\\\\\\\ AIR CONTROLS   //////////////////////
@sio.on("Air")
def airChanged(data):
    print('Air')
    # a json containing controller ids and their values
    dashValues = json.loads(data)
    if dashValues['AIRMainPwr'] == 1:
        AIRControls.AIRMain.on()
    else:
        AIRControls.AIRMain.off()





#\\\\\\\\\\\\\\\\\\\\\\ LIGHT CONTROLS   //////////////////////


@sio.on("LEDchanged")
def rangeChanged(data):
    # a json containing controller ids and their values
    dashValues = json.loads(data)
    print(dashValues)
    if dashValues['LEDGrowMainPwr'] == 1:
        LEDControls.on()
        mainDim =dashValues['LEDGrowMain']
        sup1Dim =dashValues['LEDGrowSup1']
        sup2Dim =dashValues['LEDGrowSup2']
        LEDControls.dim(mainDim,sup1Dim,sup2Dim)
    else:
        LEDControls.off()

#\\\\\\\\\\\\\\\\\\\\\\ IRRIGATION CONTROLS //////////////////////

# IRG PUMP CONTROLS
@sio.on("IRGChanged")
def IRGChanged(data):
    dashValues = json.loads(data)
    for controlId in dashValues:
        IRGControl=getattr(IRGControls,controlId)
        if dashValues[controlId] == 1:
            IRGControl.on()
        else:
            IRGControl.off()

# IRG WATER CYCLE
@sio.on('IRGCycleWtr')
def IRGCycleChanged(data):
    dashValues = json.loads(data)
    if( 'IRGWtrCycleTime' in dashValues ):
        IRGControls.waterCycle(int(dashValues['IRGWtrCycleTime']))
    else:
        IRGControls.waterCycle()

# IRG NUTRIENT CYCLE
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
@sio.on('ARMChanged')
def ArmChanged(data):
    dashValues = json.loads(data)
    global stateStepperL
    global stateStepperR
    if('swingArmL' in dashValues):
        stateStepperL = dashValues['swingArmL']
    if('swingArmR' in dashValues):
        stateStepperR = dashValues['swingArmR']

globalLoc = 0
globalCurrentLoc = 0

# ARM CALIBRATE
@sio.on('ARMCalibrate')
def ArmCalibrate(data):

    ARMControls.Callibrate()

# GO TO LOCATION
@sio.on('ARMLoc')
def ArmLocChanged(data):
    dashValues = json.loads(data)
    global globalLoc
    global globalCurrentLoc
    loc = int(dashValues['swingArmLoc'])
    globalLoc = loc
    ARMControls.goToLoc(loc)

while True:
    while stateStepperL == True:
        ARMControls.Pulsate('L')
    while stateStepperR == True:
        ARMControls.Pulsate('R')

    if (globalCurrentLoc != globalLoc):
        globalCurrentLoc = globalLoc
        ARMControls.goToLoc(globalCurrentLoc)






