################################################
## External LED Dimmer                        ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin, PWM, ADC

led = PWM(Pin(0))
pot = ADC(Pin(26))

led.freq(5000)

try:
    while True:
        pot_value = pot.read_u16()
        led.duty_u16(pot_value)
            
except KeyboardInterrupt:
    led.duty_u16(0)