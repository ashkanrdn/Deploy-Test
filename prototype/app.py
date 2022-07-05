import logging
from sched import scheduler
import sys
from datetime import datetime 
from flask import Flask, render_template, redirect, request
from models.scheduler_v2 import scheduler_v2
from models.actuators.actuator_repository import actuator_repository

app = Flask(__name__)


@app.route("/")
def index():
    scheduler_status = scheduler_v2.status
    irrigation_schedule = [cycle_time.time() for cycle_time in scheduler_v2.irrigation_schedule]
    lighting_schedule = [(lighting_on.time(),lighting_off.time()) for lighting_on, lighting_off in scheduler_v2.lighting_schedule] 
    air_schedule = [(air_on.time(), air_off.time()) for air_on, air_off in scheduler_v2.air_schedule] 
    print(lighting_schedule, air_schedule)
    return render_template('index.html', scheduler_status=scheduler_status, irrigation_schedule=irrigation_schedule, lighting_schedule=lighting_schedule, air_schedule=air_schedule)
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

@app.route("/fans/on")
def fans_on():
    actuator_repository.fans_on()
    return redirect("/")

@app.route("/fans/off")
def fans_off():
    actuator_repository.fans_off()
    return redirect("/") 

@app.route("/irg/run")
def run_water_cycle():
    actuator_repository.run_water_cycle()
    return redirect("/")

@app.route("/remove/<type>/<time>")
def remove_time(type, time):
    if type == "IRG":
        scheduler_v2.remove_irrigation_job(scheduled_time=time)
    else:
        scheduler_v2.remove_window_jobs(scheduled_window=time, job_type=type)
    scheduler_v2.initial_state()
    return redirect("/")


@app.route("/add/", methods=["POST"])
def add_time():
    job_type = request.form['type']
    try:
        
        if job_type == 'IRG':
            job_time = request.form['time']
            job_datetime = datetime.strptime(job_time, "%H:%M")
            scheduler_v2.create_irrigation_jobs([job_datetime])
        else:
            on_datetime = datetime.strptime(request.form['from'], "%H:%M")
            off_datetime = datetime.strptime(request.form['to'], "%H:%M")

            if job_type == 'LIGHT':
                scheduler_v2.create_lighting_jobs([(on_datetime, off_datetime)])
            else:
                scheduler_v2.create_air_jobs([(on_datetime, off_datetime)])

        scheduler_v2.initial_state()

    except Exception as e:
        logging.error(e)
        raise e

    
    return redirect("/")

if __name__ == '__main__':
    app.debug = True
    app.run()