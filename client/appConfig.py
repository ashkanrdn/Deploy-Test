import os
import sys
# Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))



# serverUrl = "https://amps-dash.herokuapp.com/"
serverUrl = "http://localhost:3000/"

SENSOR_CONTROLLER_SLEEPING_TIME = 3
