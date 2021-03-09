import socketio
import json

from gpiozero import LED
from time import sleep

import appConfig as config

# servo =Servo(17)

# while True:
#     servo.mid()
#     print("mid")
#     sleep(0.5)
#     servo.max()


# while True:
#


# Config file variable

server_url = config.serverUrl  # connection server URL
controlsIO = config.toggleID  # toggle controlers ID dict
controlsDimID = config.dimID  # dimmer controllers ID dict


# socket-io connections

sio = socketio.Client()
sio.connect(server_url)


def lightBool(light, lightValue):
    if type(lightValue) == bool:
        if lightValue:
            light.value = 1
        else:
            light.value = 0
    else:
        light.value = lightValue
        print(lightValue)


@sio.event
def connect():
    print("I'm connected!")


@sio.on("rangeChanged")
def rangeChanged(data):
    # a json containing controller ids and their values
    dashValues = json.loads(data)
    # looping through all the keys(controller ids) in the json emitted from server
    for controlerIDServer in dashValues:

        controlsDimID[controlerIDServer]["dimVal"] = dashValues[controlerIDServer]

        controlsDimID[controlerIDServer]["controller"].value = controlsDimID[
            controlerIDServer
        ]["dimVal"]

        print(controlsDimID[controlerIDServer]["dimVal"])