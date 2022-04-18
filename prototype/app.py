import unittest
from actuators.fan_tests import *
from actuators.irrigation_tests import *
from actuators.lighting_tests import *
# from sensors.config import FanGPIOs
import time
import streamlit as st
from IPython.display import HTML,display
# from .scheduler import Scheduler
from actuators.actuator_repository import ActuatorRepository
# import plotly.express as px

from streamlit.ScriptRunner import StopException, RerunException

#############Fans
st.markdown("<h1 style='text-align:center; color: black'>AMPS System</h1>", unsafe_allow_html=True)

def rerun():
    raise st.ScriptRunner.RerunException(st.ScriptRequestQueue.RerunData(None))

actuator_repo = ActuatorRepository()

############ FAN ################
def fan():
    fans = actuator_repo.fans
    [fan.on() for fan in fans]
    # rerun()


# #############Irrigation#############

# def irrigation():
#     irrigation_tester.setUp()
#     irrigation_tester.test_irrigation_waterCycle()
#     # rerun()

 


# ############lighting#############

# def lighting():
#     light_tester.setUp()
#     light_tester.test_dimming()
#     # rerun()

# def scheduler_run():
#     Scheduler().run()


key=1

if st.button('FAN',key=1):
    fan()
    st.write('Fan is running')
    
    

# if st.button('IRRIGATION',key=2):
#     irrigation()
#     st.write('Water is running')
    
    

# if st.button('LIGHTING',key=3):
#     lighting()
#     st.write('Light is running')
    
#     # rerun()
#     # raise RerunException()


# if st.button('RUN',key=1):
#     scheduler_run()
#     st.write('scheduler is running')