import logging
from datetime import datetime
from flask import Flask, render_template, redirect, request
from models.scheduler_v2 import scheduler_v2
from models.actuators.actuator_controller import actuator_controller

app = Flask(__name__)


@app.route("/")
def index():
    scheduler_status = scheduler_v2.status
    irrigation_schedule = [cycle_time.time() for cycle_time in scheduler_v2.irrigation_schedule]
    lighting_schedule = [(lighting_on.time(), lighting_off.time()) for lighting_on, lighting_off in
                         scheduler_v2.lighting_schedule]
    air_schedule = [(air_on_time.time(), air_off_time.time()) for air_on_time, air_off_time in scheduler_v2.air_schedule]
    print(lighting_schedule, air_schedule)
    return render_template('index.html', scheduler_status=scheduler_status, irrigation_schedule=irrigation_schedule,
                           lighting_schedule=lighting_schedule, air_schedule=air_schedule)


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
    actuator_controller.led_controller.dim()
    return redirect("/")


@app.route("/light/off")
def lights_off():
    actuator_controller.led_controller.off()
    return redirect("/")


@app.route("/air/on")
def air_on():
    actuator_controller.air_controller.on()
    return redirect("/")


@app.route("/air/off")
def air_off():
    actuator_controller.air_controller.off()
    return redirect("/")


@app.route("/irg/run")
def run_water_cycle():
    actuator_controller.irrigation_controller.run_cycle()
    return redirect("/")


@app.route("/remove/<job_type>/<time>")
def remove_time(job_type, time):
    if job_type == "IRG":
        scheduler_v2.remove_irrigation_job(scheduled_time=time)
    else:
        scheduler_v2.remove_window_jobs(scheduled_window=time, job_type=job_type)
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
