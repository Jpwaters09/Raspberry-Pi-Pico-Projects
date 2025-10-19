################################################
## Simple RGB LED                             ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin, Signal
from time import sleep

red_led = Signal(Pin(0, Pin.OUT), invert=True)
green_led = Signal(Pin(1, Pin.OUT), invert=True)
blue_led = Signal(Pin(2, Pin.OUT), invert=True)

red_led.off()
green_led.off()
blue_led.off()

try:
    while True:
        red_led.on()
        sleep(0.5)
        red_led.off()
        
        green_led.on()
        sleep(0.5)
        green_led.off()
        
        blue_led.on()
        sleep(0.5)
        blue_led.off()
        
        red_led.on()
        green_led.on()
        sleep(0.5)
        red_led.off()
        green_led.off()
        
        red_led.on()
        blue_led.on()
        sleep(0.5)
        red_led.off()
        blue_led.off()
        
        green_led.on()
        blue_led.on()
        sleep(0.5)
        red_led.off()
        green_led.off()
        
        red_led.on()
        green_led.on()
        blue_led.on()
        sleep(0.5)
        red_led.off()
        green_led.off()
        blue_led.off()
        
except KeyboardInterrupt:
    red_led.off()
    green_led.off()
    blue_led.off()
