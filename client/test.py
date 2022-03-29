import time
import datetime

min = 21

timeList = ["15:23:20", "15:23:30", "15:23:55"]
timeList2 = ['15:34:05']

while True:
    dateSTR = datetime.datetime.now().strftime("%H:%M:%S")
    if dateSTR in timeList:
        print(dateSTR)
        time.sleep(2)
    elif dateSTR in timeList2:
        print(dateSTR)
        time.sleep(2)
    

