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
controlsDim = config.dimID  # dimmer controllers ID dict


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
    for controlIDServer in dashValues:
        # selecting toggle controllers by comparing keys from server with
        #  a dictionary containing all the toggle controllers
        if controlIDServer in controlsIO:
            controlsIO[controlIDServer]["state"] = dashValues[controlIDServer]
            lightBool(
                controlsIO[controlIDServer]["controller"],
                controlsIO[controlIDServer]["state"],
            )
        elif controlIDServer in controlsDim:
            controlsDim[controlIDServer]["dimVal"] = dashValues[controlIDServer]

            lightBool(
                controlsDim[controlIDServer]["controller"],
                controlsDim[controlIDServer]["dimVal"],
            )

            print(controlsDim[controlIDServer]["dimVal"])