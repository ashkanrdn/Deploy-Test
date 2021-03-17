import gpiozero
from time import sleep

sensrL = gpiozero.InputDevice(11 ,pull_up= True)
counter= 0
while True:
    if (sensrL.is_active == True):

        counter += 1
        sleep(1)
        print('touch')
        if counter == 10:
            break


print(counter)