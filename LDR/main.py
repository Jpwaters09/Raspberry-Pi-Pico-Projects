################################################
## LDR                                        ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin, ADC
from time import sleep

ldr = ADC(Pin(26))

try:
    while True:
        ldr_value = ldr.read_u16()
        
        print(f"LDR Value: {ldr_value}\n")
        
        sleep(0.5)
        
except KeyboardInterrupt:
    pass
