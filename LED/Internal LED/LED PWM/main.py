################################################
## Internal LED PWM                           ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin, PWM
from time import sleep

# Change the number below to change the speed #
duty_step = 250                               #
###############################################

led = PWM(Pin("LED"))

led.freq(5000)

try:
    while True:
        for duty_cycle in range(0, 65536, duty_step):
            led.duty_u16(duty_cycle)
            sleep(0.005)
            
        for duty_cycle in range(65536, 0, -duty_step):
            led.duty_u16(duty_cycle)
            sleep(0.005)
            
except KeyboardInterrupt:
    pass
