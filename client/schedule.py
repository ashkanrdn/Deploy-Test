from time import sleep
import json
import socketio
import os
import sys

import time
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
# Modify PATH so we can import files from elsewhere in this direcotry
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

scheduler = BlockingScheduler()


server_url = "http://localhost:3000/"


routines = []

mamad = 'my_job_id'

# routine_number is for the predefined funcs (wtr,nutr,light,...), job id has to be stored somewhere so it can br retrieved to be modify task


def schedule_task(routine_number, task_id, task_args, task_day_of_week, task_hour, task_minute):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    scheduler.add_job(func=routines[routine_number], trigger='cron', args=task_args,
                      day_of_week=task_day_of_week, hour=task_hour, minute=task_minute,
                      id=task_id)  # Add task


def test_job(test_arg):
    print(test_arg)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


routines.append(test_job)


# scheduler.reschedule_job(job_id=mamad, trigger='cron', minute='*/5')

sio = socketio.Client()
sio.connect(server_url)


@sio.event
def connect():
    print("AMPS Conntected to Control Dashboard!")
    # ARMControls.Callibrate()


# \\\\\\\\\\\\\\\\\\\\\\ AIR CONTROLS   //////////////////////
@sio.on("scheduleWTR")
def scheduleWTRChanged(data):
    # print('Air')
    # a json containing controller ids and their values
    dashValues = json.loads(data)
    print(dashValues)

    # schedule_task(routine_number=dashValues['routine_number'],
    #               task_id=dashValues['task_id'],
    #               task_args=dashValues['task_args'],
    #               task_day_of_week=dashValues['day_of_week'],
    #               task_hour=dashValues['task_hour'],
    #               task_minute=dashValues['task_minute'])


@sio.on("ARMChanged")
def armChanged(data):
    # print('Air')
    # a json containing controller ids and their values
    dashValues = json.loads(data)
    print(dashValues)
    print('________________________')
    # scheduler.print_jobs()
    # print('________________________')

    # scheduler.remove_job(dashValues['task_id'])  # Delete task
    # print('________________________')
    # scheduler.print_jobs()


# goal is to make pre made functions and call them from dash
# and pass arguments from data to the scheduler function
# this should work for now


# functions=['water','nutrient','air','arm','light']
# time.sleep(60*7)


# scheduler.remove_job('my_job_id')  # Delete task
# scheduler.pause_job('my_job_id')  # Tentative task
# scheduler.resume_job('my_job_id')  # Recovery task

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=19, minute=59 )


# @scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=19, minute=58 )
# def my_job1():
#     print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#     print('yoho')


# decorator = decorator_function(display)


# def outer_func(passed_func):
#     def wrapperfunc(passed_func):
#         return passed_func()
#     return wrapperfunc(passed_func)

# @outer_func
# def wrapper():
#     print('sikim')
scheduler.start()
