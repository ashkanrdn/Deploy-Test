import sys

from flask import Flask, render_template, redirect
from models.scheduler_v2 import scheduler_v2
from models.actuators.actuator_repository import actuator_repository

app = Flask(__name__)


@app.route("/")
def index():
    scheduler_status = scheduler_v2.status
    return render_template('index.html', scheduler_status=scheduler_status)
    # return f"<h1>Hello Worlld {scheduler_status}</h1>"


@app.route("/scheduler/on")
def start_scheduler():
    scheduler_v2.start()
    return redirect("/")


@app.route("/scheduler/off")
def stop_scheduler():
    scheduler_v2.pause()
    return redirect("/")

@app.route("/light/on")
def lights_on():
    actuator_repository.main_led.on()
    return redirect("/")

@app.route("/light/off")
def lights_off():
    actuator_repository.main_led.off()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)