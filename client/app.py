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


# standard Python
server_url = config.serverUrl
controlsIO = config.toggleID
sio = socketio.Client()
sio.connect(server_url)


@sio.event
def connect():
    print("I'm connected!")


@sio.on('rangeChanged')
def rangeChanged(data):
    dashValues = json.loads(data)
    for controlIDServer in dashValues:
        if (controlIDServer in controlsIO):
            print(controlIDServer)
            print(controlsIO)
            controlsIO[controlIDServer]['val'] = dashValues[controlIDServer]



    # print(controlsIO,'mmd')