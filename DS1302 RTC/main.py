################################################
## DS1302 RTC                                 ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin
from ds1302 import DS1302
from time import localtime, sleep

ds = DS1302(Pin(2), Pin(1), Pin(0))

def setCurrentDate():
    currentTime = localtime()

    year = currentTime[0]
    month = currentTime[1]
    day = currentTime[2]
    hour = currentTime[3]
    minute = currentTime[4]
    second = currentTime[5]
    weekday = currentTime[6] + 1

    ds.date_time([year, month, day, weekday, hour, minute, second])

# Set Current Date #
setCurrentDate()   #
####################

try:
    while True:
        RTCday = ds.day()
        RTCmonth = ds.month()
        RTCyear = ds.year()
        RTChour = ds.hour()
        RTCminute = ds.minute()

        print(f"Current Date: {RTCday}/{RTCmonth}/{RTCyear}")
        print(f"CurrentTime: {RTChour}:{RTCminute}\n")
        
        sleep(1)

except KeyboardInterrupt:
    pass