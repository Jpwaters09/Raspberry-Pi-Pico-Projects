################################################
## RGB LED Dimmer                             ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin, PWM, ADC

red_led = PWM(Pin(0, Pin.OUT))
green_led = PWM(Pin(1, Pin.OUT))
blue_led = PWM(Pin(2, Pin.OUT))

pot1 = ADC(Pin(26))
pot2 = ADC(Pin(27))
pot3 = ADC(Pin(28))

red_led.freq(5000)
green_led.freq(5000)
blue_led.freq(5000)

try:
    while True:
        pot1_value = pot1.read_u16()
        pot2_value = pot2.read_u16()
        pot3_value = pot3.read_u16()
        
        red_led.duty_u16(pot1_value)
        green_led.duty_u16(pot2_value)
        blue_led.duty_u16(pot3_value)
        
except KeyboardInterrupt:
    pass
