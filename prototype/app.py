from flask import Flask, render_template
from scheduler_v2 import scheduler_v2

app = Flask(__name__)


@app.route("/")
def index():
    scheduler_status = scheduler_v2.status
    render_template('index.html', scheduler_status=scheduler_status)


@app.route("/startScheduler", methods=['POST'])
def start_scheduler():
    scheduler_v2.run()


@app.route("/stopScheduler", methods=['POST'])
def stop_scheduler():
    scheduler_v2.pause()
