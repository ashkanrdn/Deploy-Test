from gpiozero import PWMLED


# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"


LEDGrowMainPWR = PWMLED(17)
LEDGrowSup1PWR = PWMLED(27)
LEDGrowSup2PWR = PWMLED(22)

toggleID = {
    "LEDGrowMainPWR": {"controller": LEDGrowMainPWR, "state": False},
    "LEDGrowSup1PWR": {"controller": LEDGrowSup1PWR, "state": False},
    "LEDGrowSup2PWR": {"controller": LEDGrowSup2PWR, "state": False},
}

dimID = {
    "LEDGrowMain": {"controller": LEDGrowMainPWR, "dimVal": 0},
    "LEDGrowSup1": {"controller": LEDGrowSup1PWR, "dimVal": 0},
    "LEDGrowSup2": {"controller": LEDGrowSup2PWR, "dimVal": 0},
}