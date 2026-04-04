################################################
## Internal LED Toggle                        ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2026 Jacob Waters            ##
## Contact me: contact.jpwaters09@gmail.com   ##
################################################

from machine import Pin

led = Pin("LED", Pin.OUT)

led.toggle()
