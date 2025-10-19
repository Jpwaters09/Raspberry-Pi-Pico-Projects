################################################
## DHT11                                      ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(0))

try:
    while True:
        try:
            sensor.measure()
            temp = sensor.temperature()
            humidity = sensor.humidity()
            
            print(f"Temperature: {temp}C")
            print(f"Humidity: {humidity}%\n")
            
            sleep(1)
        
        except OSError:
            print("Failed to read sensor.")
            sleep(1)
        
except KeyboardInterrupt:
    pass
