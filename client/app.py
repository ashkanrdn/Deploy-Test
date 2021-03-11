# # Modify PATH so we can import files from elsewhere in this repo
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

controlsDimID = config.dimID  # dimmer controllers ID dict
lightingControls = LedMain(gpioPwr = , gpioDim, gpioSupp1, gpioSupp2, ledSuppOneDim = 0.5, ledSuppTwoDim = 0.5 , ledMainDim = 0.5):



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
    # looping through all the keys(controller ids) in the json emitted from server
    for controlerIDServer in dashValues:
        # updating the values in the controller dictionary
        controlsDimID[controlerIDServer]["dimVal"] = dashValues[controlerIDServer]
        # changing the dim value
        controlsDimID[controlerIDServer]["controller"].value = controlsDimID[controlerIDServer]["dimVal"]

        print(controlsDimID[controlerIDServer]["dimVal"])