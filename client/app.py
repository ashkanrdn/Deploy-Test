import logging
from datetime import datetime
from flask import Flask, render_template, redirect, request
from .models.actuators.actuator_scheduler import actuator_scheduler
# from models.sensors.sensor_scheduler import sensor_scheduler
from .models.actuators.actuator_controller import actuator_controller

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', scheduler_status=actuator_scheduler.status,
                           irrigation_schedule=actuator_scheduler.irrigation_schedule,
                           lighting_schedule=actuator_scheduler.lighting_schedule,
                           air_schedule=actuator_scheduler.air_schedule)


@app.route("/scheduler/on")
def start_scheduler():
    actuator_scheduler.start()
    # sensor_scheduler.start()

    return redirect("/")


@app.route("/scheduler/off")
def stop_scheduler():
    actuator_scheduler.pause()
    # sensor_scheduler.pause()

    return redirect("/")


@app.route("/light/on")
def lights_on():
    actuator_controller.led_controller.power_on()
    return redirect("/")


@app.route("/light/off")
def lights_off():
    actuator_controller.led_controller.power_off()
    return redirect("/")


@app.route("/air/on")
def air_on():
    actuator_controller.air_controller.on()
    return redirect("/")


@app.route("/air/off")
def air_off():
    actuator_controller.air_controller.off()
    return redirect("/")


@app.route("/irg/run", methods=['POST'])
def run_water_cycle():
    duration = int(request.form['duration'])
    print(duration)
    # level = int(request.form['level'])
    # TODO add only choosing that level
    # actuator_scheduler.run_immediate_irrigation_job(duration=duration)
    actuator_controller.irrigation_controller.run_cycle(duration=duration)

    return redirect("/")


@app.route("/remove/<job_type>/<time>")
def remove_time(job_type, time):
    if job_type == "IRG":
        actuator_scheduler.remove_irrigation_job(scheduled_time=time)
    else:
        actuator_scheduler.remove_window_jobs(scheduled_window=time, job_type=job_type)
    return redirect("/")


@app.route("/add/", methods=["POST"])
def add_time():
    job_type = request.form['type']
    try:

        if job_type == 'IRG':
            job_time = request.form['time']
            job_duration = int(request.form['duration'])
            job_datetime = datetime.strptime(job_time, "%H:%M")
            actuator_scheduler.add_irrigation_jobs([(job_datetime, job_duration)])
        else:
            on_datetime = datetime.strptime(request.form['from'], "%H:%M")
            off_datetime = datetime.strptime(request.form['to'], "%H:%M")

            if job_type == 'LIGHT':
                actuator_scheduler.add_lighting_jobs([(on_datetime, off_datetime)])
            elif job_type == 'AIR':
                actuator_scheduler.add_air_jobs([(on_datetime, off_datetime)])


    except Exception as e:
        logging.error(e)
        raise e

    return redirect("/")


if __name__ == '__main__':
    app.debug = True
    app.run()

# actuator_scheduler.start()
# while True:
#     pass