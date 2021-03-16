import gpiozero
import time
from time import sleep



sol = gpiozero.OutputDevice(10)


sol.on()
sleep(2)
sol.off()

