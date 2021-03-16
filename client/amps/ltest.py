from gpiozero import PWMLED
from time import sleep

led = PWMLED(25)

for i in range(10):

    led.value = i/10  # off
    sleep(1)

