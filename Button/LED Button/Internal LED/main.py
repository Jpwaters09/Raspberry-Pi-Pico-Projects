################################################
## Internal LED Button                        ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin
from time import sleep

button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin("LED", Pin.OUT)

try:
    while True:
        if not button.value():
            led.toggle()
            sleep(0.5)
        
except KeyboardInterrupt:
    pass