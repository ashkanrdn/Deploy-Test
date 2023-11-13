import sqlite3
from datetime import datetime

class SchedulerDB:
    def __init__(self, name) -> None:
        self.name = name

    def connect_db(self):
        return sqlite3.connect(self.name)
    
    def insert_irrigation_job(self, type, start_time, duration):
        conn = self.connect_db()
        with conn:
            conn.execute('INSERT INTO schedules (type, start_time, duration) VALUES (?, ?, ?)',
                        (type, start_time, duration))
        conn.close()

    def insert_window_jobs(self, type, start_time, end_time):
        conn = self.connect_db()
        with conn:
            conn.execute('INSERT INTO schedules (type, start_time, end_time) VALUES (?, ?, ?)',
                        (type, start_time, end_time))
        conn.close() 


    def read_jobs(self, job_type):
        conn = self.connect_db()
        cursor = conn.cursor()
        if job_type in ('IRG', 'FER'):
            cursor.execute('SELECT id, start_time, duration FROM schedules WHERE type = ?', (job_type,))
        else:
            cursor.execute('SELECT id, start_time, end_time FROM schedules WHERE type = ?', (job_type,))

        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_job(self, job_type, start_time):
        conn = self.connect_db()
        with conn:
            conn.execute('DELETE FROM schedules WHERE type = ? AND start_time', (job_type, start_time))
        conn.close()

    
    def load_jobs(self):
        IRRIGATION_SCHEDULE = self.read_jobs('IRG')
        LIGHTING_SCHEDULE = self.read_jobs('LIGHT')
        FAN_SCHEDULE = self.read_jobs('FAN')
        irrigation_schedule = [(datetime.strptime(start_time, "%H:%M:%S"), duration) for id, start_time, duration in
                               IRRIGATION_SCHEDULE]
        
        lighting_schedule = [(datetime.strptime(start_time, "%H:%M:%S"), datetime.strptime(end_time, "%H:%M:%S"))
                             for id, start_time, end_time in LIGHTING_SCHEDULE]
        fan_schedule = [(datetime.strptime(start_time, "%H:%M:%S"), datetime.strptime(end_time, "%H:%M:%S"))
                        for id, start_time, end_time in FAN_SCHEDULE]
        
        return irrigation_schedule, lighting_schedule, fan_schedule


db = SchedulerDB('schedules.db')            



    