import time
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()



@sched.scheduled_job('cron', day_of_week='mon-fri', hour=19, minute=59 )
def my_job():
    print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print('yohaaao')


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=19, minute=58 )
def my_job1():
    print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print('yoho')


sched.start()