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

red= LED(27)

# while True:
#



# standard Python
server_url = config.serverUrl

sio = socketio.Client()
sio.connect(server_url)


@sio.event
def connect():
    print("I'm connected!")


@sio.on('rangeChanged')
def rangeChanged(data):
    mamad = json.loads(data)
    for key in mamad:
        if (key == 'LEDGrowMainPWR'):
            if(mamad[key] == True):
                red.on()
            elif(mamad[key] == False):
                red.off()




