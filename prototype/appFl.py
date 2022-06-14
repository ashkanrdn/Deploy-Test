from flask import Flask
import streamlit as st
import pandas as pd
import numpy as np

# import plotly.express as px
# from plotly.subplots import make_subplots
# import plotly.graph_objects as graph_objects
from numpy import e

# app= Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"
    
# print("Hello")
# if __name__=="main":
#     app.run(host='0.0.0.0',port=80,debug=True)