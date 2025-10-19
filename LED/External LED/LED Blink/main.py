################################################
## External LED Blink                         ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin
from time import sleep

# Change the number below to change the delay in seconds #
delay = 0.5                                              #
##########################################################

led = Pin(0, Pin.OUT)

try:
    while True:
        led.toggle()
        
        sleep(delay)

except KeyboardInterrupt:
    led.off()
