from gpiozero import LED

LEDGrowMainPWR= LED(17)

# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"

toggleID ={'LEDGrowMainPWR': {'controller' : 'mamd' , 'val' : False} }
# print(toggleID['LEDGrowMainPWR']['controller'])