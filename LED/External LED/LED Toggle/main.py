################################################
## External LED Toggle                        ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2026 Jacob Waters            ##
## Contact me: contact.jpwaters09@gmail.com   ##
################################################

from machine import Pin

led = Pin(0, Pin.OUT)

led.toggle()
