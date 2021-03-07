import gpiozero
import time
from time import sleep

sensor = gpiozero.Button(11)

while True:
    sleep(.1)
    if sensor.is_pressed:
        print("sensed")
    else:
        print("nope")



