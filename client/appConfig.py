from gpiozero import PWMLED


# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"




LEDGrowMainPWR=PWMLED(17)
LEDGrowSup1PWR=PWMLED(27)
LEDGrowSup2PWR=PWMLED(22)

toggleID = {
    "LEDGrowMainPWR": {"controller": LEDGrowMainPWR, "state": False},
    "LEDGrowSup1PWR": {"controller": LEDGrowSup1PWR, "state": True},
    "LEDGrowSup2PWR": {"controller": LEDGrowSup2PWR, "state": False},
}
