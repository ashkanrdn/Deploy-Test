import gpiozero
import time

pSensor1 = gpiozero.InputDevice(8, pull_up=True)
pSensor2 = gpiozero.InputDevice(11, pull_up=True)
light = gpiozero.OutputDevice(22)

light.on()
time.sleep(0.5)
light.off()
while True:
    if pSensor1.is_active == True:
        light.on()
        #print('sensor triggered')
        #break
    if pSensor1.is_active == False:
        light.off()
        #print('not sensed')
    if pSensor2.is_active == True:
        light.on()
        #print('sensor triggered')
        #break
    if pSensor2.is_active == False:
        light.off()
        #print('not sensed')

        
