################################################
## Ultrasonic Sensor                          ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin
from utime import sleep_us, ticks_us
from time import sleep

echo = Pin(0, Pin.IN)
trigger = Pin(1, Pin.OUT)

try:
    while True:
        trigger.low()
        sleep_us(2)
        trigger.high()
        sleep_us(5)
        trigger.low()
        
        while not echo.value():
            signalOff = ticks_us()
            
        while echo.value():
            signalOn = ticks_us()
            
        timePassed = signalOn - signalOff
        distance = round(((timePassed * 0.0343) / 2), 2)
        
        print(f"Distance: {distance}cm")
        
        sleep(1)
        
except KeyboardInterrupt:
    pass
