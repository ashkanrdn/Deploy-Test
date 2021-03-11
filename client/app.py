
import os
import sys
 # Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))


import socketio
import json

from gpiozero import LED
from time import sleep

import appConfig as config

from amps.lightingClass import LedMain


# Config file variable

server_url = config.serverUrl  # connection server URL



gpioLedODMainPwr =  config.gpioLedODMainPwr
gpioLedPWMMainDim =  config.gpioLedPWMMainDim
gpioLedPWMSup1Dim = config.gpioLedPWMSupOneDim
gpioLedPWMSup2Dim= config.gpioLedPWMSupTWoDim

lightingControls = LedMain(gpioPwr = gpioLedODMainPwr , gpioDim = gpioLedPWMMainDim , gpioSupp1 = gpioLedPWMSup1Dim, gpioSupp2 = gpioLedPWMSup2Dim)

dimID = {


    "LEDGrowMainPwr": {"controller": lightingControls.lightingLedMainPWR, "dimVal": 0},

    "LEDGrowMain": {"controller": lightingControls.lightingLedMain, "dimVal": 0},
    "LEDGrowSup1": {"controller": lightingControls.lightingLedSuppOne, "dimVal": 0},
    "LEDGrowSup2": {"controller": lightingControls.lightingLedSuppTwo, "dimVal": 0},
}


# socket-io connections

sio = socketio.Client()
sio.connect(server_url)


@sio.event
def connect():
    print("I'm connected!")


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
    # looping through all the keys(controller ids) in the json emitted from server

    # for controlerIDServer in dashValues:
    print(dashValues)

    # if(dashValues['LEDGrowMainPwr'] == 0):
    #     lightingControls.off()
    # print(dashValues['lightingMainControls'],'shab')




        # dimVal= dashValues[controlerIDServer]
        # if controlerIDServer == 'lightingMainControls':
        #     # lightingControls.dim(dimVal)
        #     lightingControls.on()

        # elif (controlerIDServer == 'LEDGrowMain'):
        #     if (dashValues['LEDGrowMain'] > 0):
        #         dimID['LEDGrowMainPwr']['controller'].on()
        #         dimID['LEDGrowMain']['controller'].value= dimVal
        #     elif (dashValues['LEDGrowMain'] == 0):
        #         dimID['LEDGrowMainPwr']['controller'].off()
        #         dimID['LEDGrowMain']['controller'].value= dimVal
        # else:


        #     # updating the values in the controller dictionary
        #     dimID[controlerIDServer]["dimVal"] =dimVal
        #     # changing the dim value
        #     dimID[controlerIDServer]["controller"].value = dimID[controlerIDServer]["dimVal"]

        #     print(dimID[controlerIDServer]["dimVal"])