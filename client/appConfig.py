<<<<<<< HEAD
from gpiozero import LED

LEDGrowMainPWR= LED(17)

# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"

toggleID ={'LEDGrowMainPWR': {'controller' : 'mamd' , 'val' : False} }
# print(toggleID['LEDGrowMainPWR']['controller'])
=======
# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"
# ,'LEDGrowSup2PWR':{'controller' : 'mamad', 'state' : True}
toggleID = {
    "LEDGrowMainPWR": {"controller": "LEDGrowMainPWR", "state": True},
    "LEDGrowSup1PWR": {"controller": "LEDGrowSup1PWR", "state": True},
    "LEDGrowSup2PWR": {"controller": "LEDGrowSup2PWR", "state": True},
}
>>>>>>> 555d48a144265b855c91c596f4910c3b9c98d8c3
