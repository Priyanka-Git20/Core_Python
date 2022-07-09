'''
   @Author : Priyanka Salunkhe
   @Date : 2022-07-07  17:00:00
   @Last Modified by : Priyanka Salunkhe
   @Last Modified Time : 2022-07-07  17:30:00
   @Title : Calculate elapses time between start time and stop time of the timer.
'''


import time
import datetime


def elapsed_time_calculation():
    """
        Description:
            Measuring the time that elapses between the start and end click
        Parameter:
            None
        Return:
            Returning nothing printing elasped time
    """
    start = input("Press Enter to start ")
    print("Timer has started")
    startTime = time.time()
    stop = input("Press Enter to stop ")
    print("Timer has stoped")
    endTime = time.time()
    elaspedTime = str(datetime.timedelta(seconds = endTime -startTime))
    elaspedTime1 = str(endTime - startTime)
    print("Elasped time is ",elaspedTime,elaspedTime1)

elapsed_time_calculation()