# \\\\\\\\\\\\\\\\\\\\\\ AMPS IMPORTS //////////////////////
from logging import error
from amps.AIR import AIR
from amps.ARM import ARM
from amps.IRG import Irrigation as IRG
from amps.LED import LedMain as LED
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

from apscheduler.schedulers.background import BackgroundScheduler


from appConfig import *
# Modify PATH so we can import files from elsewhere in this direcotry
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))


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
    logging.INFO("AMPS Connected to Control Dashboard!")
    # ARMControls.Callibrate()


# \\\\\\\\\\\\\\\\\\\\\\ AIR CONTROLS   //////////////////////
@sio.on("AIRChanged")
def airChanged(data):

    # a json containing controller ids and their values
    dashValues = json.loads(data)
    if dashValues['AIRMainPwr'] == 1:
        actuator_controller.air_controller.AIRMain.on()
    else:
        actuator_controller.air_controller.AIRMain.off()


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
        actuator_controller.led_controller.off()


# \\\\\\\\\\\\\\\\\\\\\\ IRRIGATION CONTROLS //////////////////////

# IRG PUMP CONTROLS


@sio.on("IRGChanged")
def IRGChanged(data):
    dashValues = json.loads(data)
    for controlId in dashValues:
        actuator_controller.IRGControl = getattr(actuator_controller.irrigation_controller, controlId)
        if dashValues[controlId] == 1:
            actuator_controller.IRGControl.on()
        else:
            actuator_controller.irrigation_controller.power_off()


# IRG WATER CYCLE


@sio.on('IRGCycleWtr')
def IRGCycleChanged(data):
    print('water cycle activated')
    dashValues = json.loads(data)
    if ('IRGWtrCycleTime' in dashValues):
        actuator_controller.irrigation_controller.run_water_cycle(int(dashValues['IRGWtrCycleTime']))
    else:
        actuator_controller.irrigation_controller.run_water_cycle()


# IRG NUTRIENT CYCLE


@sio.on('IRGCycleNutr')
def IRGCycleChangedNutr(data):
    dashValues = json.loads(data)
    if ('IRGNutrCycleTime' in dashValues):
        actuator_controller.irrigation_controller.nutrientCycle(int(dashValues['IRGNutrCycleTime']))
    else:
        actuator_controller.irrigation_controller.nutrientCycle()


# \\\\\\\\\\\\\\\\\\\\\\ ARM CONTROLS //////////////////////


stateStepperL = False
stateStepperR = False
globalLoc = 0
globalCurrentLoc = 0
# STEP TP L/R


@sio.on('ARMChanged')
def ArmChanged(data):
    dashValues = json.loads(data)
    global stateStepperL
    global stateStepperR


# Note : if the while true runs on the main app it causes the 
# calibrate function to run slowly without while true maual jog to 
# left or right and go to loc is not possible
# research asyncio and back ground tasks to see if the args from event can be passed
# some async runner in the bg and keep the thread alive
    
  
    if('swingArmL' in dashValues == True):

        stateStepperL = dashValues['swingArmL']
        actuator_controller.arm_controller.Pulsate(dir='L')
        print('move left',actuator_controller.arm_controller.ARMLoc)


    if('swingArmR' in dashValues == True):
        stateStepperR = dashValues['swingArmR']
        actuator_controller.arm_controller.Pulsate(dir='R')
        print('move right', globalCurrentLoc)






# ARM CALIBRATE


@sio.on('ARMCalibrate')
def ArmCalibrate(data):
    print('Calibrating ')
    print (' global loc current ', globalCurrentLoc)

    print (' global loc ', globalLoc)
    print (' global loc current ', globalCurrentLoc)
    actuator_controller.arm_controller.Callibrate()

# GO TO LOCATION


@sio.on('ARMLoc')
def ArmLocChanged(data):
    dashValues = json.loads(data)
    
    global globalLoc
    global globalCurrentLoc
    loc = int(dashValues['swingArmLoc'])
    globalLoc = loc
    # ARMControls.goToLoc(loc)








# sched = BackgroundScheduler()
#
#
# @sched.scheduled_job('cron', day_of_week='mon-tue,fri-sat', hour='*/8')
# def water_Schedule_1():
#     logging.INFO(('Water Cycle ran @ ') +
#                  (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
#     actuator_controller.irrigation_controller.run_water_cycle()
#
#
# @sched.scheduled_job('cron', day_of_week='wed-thu,sun', hour='*/12')
# def water_Schedule_2():
#     logging.INFO(('Water Cycle ran @ ') +
#                  (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
#     actuator_controller.irrigation_controller.run_water_cycle()
#
#
# @sched.scheduled_job('cron', hour=23, minute=45)
# def nutrient_Schedule():
#     logging.INFO(('nutrient Cycle ran @ ') +
#                  (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
#     actuator_controller.irrigation_controller.nutrientCycle()
#
#
# @sched.scheduled_job('cron', day="*" , hour = "6")
# def LED_Schedule_on():
#     print(('Lights turned on ')+ (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) )
#     actuator_controller.led_controller.on()
#     # LEDControls.dim(1, 1, 1)
#
# @sched.scheduled_job('cron', day="*" , hour = "20")
# def LED_Schedule_off():
#     print(('Lights turned off ')+ (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) )
#     actuator_controller.led_controller.off()

# @sched.scheduled_job('cron', day_of_week="mon-fri" , hour = "8")
# def AIR_Schedule_on():
#     print(('Lights turned on ')+ (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) )
#     AIRControls.AIRMain.on()

# @sched.scheduled_job('cron', day_of_week="mon-fri" , hour = "8")
# def AIR_Schedule_off():
#     print(('Lights turned off ')+ (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) )
#     AIRControls.AIRMain.off()

# sched.start()
# print(" Pi started")
# for i in range(663311):
#     ARMControls.Pulsate("L")
# while True:

#     while stateStepperL == True:
#         ARMControls.Pulsate('L')
#     while stateStepperR == True:
#         ARMControls.Pulsate('R')


#     if (globalCurrentLoc != globalLoc):
#         globalCurrentLoc = globalLoc
#         ARMControls.goToLoc(globalCurrentLoc)
# print(ARMControls.ARMLoc)

# # ARMControls.Callibrate()
# print("Calibrating")
# ARMControls.goToLoc(10)
# print(ARMControls.ARMLoc)

# LEDControls.on()
# LEDControls.dim(1, 1, 1)
# time.sleep(3)
# LEDControls.dim(0, 0, 1)
# time.sleep(3)
# LEDControls.dim(0, 1, 0)
# time.sleep(3)
# LEDControls.dim(1, 0, 0)
# time.sleep(3)
# LEDControls.dim(0, 0, 0)
# LEDControls.off()












