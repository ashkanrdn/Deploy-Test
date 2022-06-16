import appConfig as config
import logging
from actuators.actuator_controller import ActuatorController
from time import sleep
from gpiozero import LED
import json
import socketio
import os
import sys

import time
from apscheduler.schedulers.blocking import BlockingScheduler
from appConfig import *
# Modify PATH so we can import files from elsewhere in this direcotry
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))
# \\\\\\\\\\\\\\\\\\\\\\ AMPS IMPORTS //////////////////////


# # Config file variable
server_url = config.serverUrl  # connection server URL

# \\\\\\\\\\\\\\\\\\\\\\ CONTROL CLASS INSTANTIATE //////////////////////


logging.basicConfig(filename='logTest.log', level=logging.INFO)
# \\\\\\\\\\\\\\\\\\\\\\ SOCKET INIT //////////////////////

actuator_controller = ActuatorController()

sio = socketio.Client()
sio.connect(server_url)


# \\\\\\\\\\\\\\\\\\\\\\ SOCKET CONNECTION   //////////////////////


@sio.event
def connect():
    logging.INFO("AMPS Conntected to Control Dashboard!")
    # ARMControls.Callibrate()


# \\\\\\\\\\\\\\\\\\\\\\ AIR CONTROLS   //////////////////////
@sio.on("AIRChanged")
def airChanged(data):
    print('Air')
    # a json containing controller ids and their values
    dashValues = json.loads(data)
    if dashValues['AIRMainPwr'] == 1:
        actuator_controller.AIRControls.AIRMain.on()
    else:
        actuator_controller.AIRControls.AIRMain.off()


# \\\\\\\\\\\\\\\\\\\\\\ LIGHT CONTROLS   //////////////////////


@sio.on("LEDchanged")
def rangeChanged(data):
    # a json containing controller ids and their values
    dashValues = json.loads(data)
    logging.INFO(dashValues)
    if dashValues['LEDGrowMainPwr'] == 1:
        actuator_controller.LEDControls.on()
        mainDim = dashValues['LEDGrowMain']
        sup1Dim = dashValues['LEDGrowSup1']
        sup2Dim = dashValues['LEDGrowSup2']
        actuator_controller.LEDControls.dim(mainDim, sup1Dim, sup2Dim)
    else:
        actuator_controller.LEDControls.off()


# \\\\\\\\\\\\\\\\\\\\\\ IRRIGATION CONTROLS //////////////////////

# IRG PUMP CONTROLS


@sio.on("IRGChanged")
def IRGChanged(data):
    dashValues = json.loads(data)
    for controlId in dashValues:
        actuator_controller.IRGControl = getattr(IRGControls, controlId)
        if dashValues[controlId] == 1:
            actuator_controller.IRGControl.on()
        else:
            actuator_controller.IRGControl.power_off()


# IRG WATER CYCLE


@sio.on('IRGCycleWtr')
def IRGCycleChanged(data):
    dashValues = json.loads(data)
    if ('IRGWtrCycleTime' in dashValues):
        actuator_controller.IRGControls.run_water_cycle(int(dashValues['IRGWtrCycleTime']))
    else:
        actuator_controller.IRGControls.run_water_cycle()


# IRG NUTRIENT CYCLE


@sio.on('IRGCycleNutr')
def IRGCycleChangedNutr(data):
    dashValues = json.loads(data)
    if ('IRGNutrCycleTime' in dashValues):
        actuator_controller.IRGControls.nutrientCycle(int(dashValues['IRGNutrCycleTime']))
    else:
        actuator_controller.IRGControls.nutrientCycle()


# \\\\\\\\\\\\\\\\\\\\\\ ARM CONTROLS //////////////////////


stateStepperL = False
stateStepperR = False


# STEP TP L/R


@sio.on('ARMChanged')
def ArmChanged(data):
    dashValues = json.loads(data)
    global stateStepperL
    global stateStepperR
    if ('swingArmL' in dashValues):
        stateStepperL = dashValues['swingArmL']
    if ('swingArmR' in dashValues):
        stateStepperR = dashValues['swingArmR']


globalLoc = 0
globalCurrentLoc = 0


# ARM CALIBRATE


@sio.on('ARMCalibrate')
def ArmCalibrate(data):
    actuator_controller.ARMControls.calibrate()


# GO TO LOCATION


@sio.on('ARMLoc')
def ArmLocChanged(data):
    dashValues = json.loads(data)
    global globalLoc
    global globalCurrentLoc
    loc = int(dashValues['swingArmLoc'])
    globalLoc = loc
    actuator_controller.ARMControls.go_to_loc(loc)


sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-tue,fri-sat', hour='*/8')
def water_Schedule_1():
    logging.INFO(('Water Cycle ran @ ') +
                 (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    actuator_controller.IRGControls.run_water_cycle()


@sched.scheduled_job('cron', day_of_week='wed-thu,sun', hour='*/12')
def water_Schedule_2():
    logging.INFO(('Water Cycle ran @ ') +
                 (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    actuator_controller.IRGControls.run_water_cycle()


@sched.scheduled_job('cron', hour=23, minute=45)
def nutrient_Schedule():
    logging.INFO(('nutrient Cycle ran @ ') +
                 (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    actuator_controller.IRGControls.nutrientCycle()


sched.start()

while True:
    while stateStepperL == True:
        actuator_controller.ARMControls.pulsate('L')
    while stateStepperR == True:
        actuator_controller.ARMControls.pulsate('R')

    if (globalCurrentLoc != globalLoc):
        globalCurrentLoc = globalLoc
        actuator_controller.ARMControls.go_to_loc(globalCurrentLoc)
