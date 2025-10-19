# Ultrasonic Module:
Schematic - See below the schematic for instructions:
 
![](Schematic.png)
 
What You Will Need:
- 1 x Raspberry Pi Pico
- 1 x Breadboard
- 4 x Jumper Wires
- 1 x HC-SR04 Ultrasonic Module

Setting Up The Circuit:
1. Make the circuit: \
   HC-SR04 VCC(+) => 3.3v On Raspberry Pi Pico \
   HC-SR04 Trigger => GPIO 1 On Raspberry Pi Pico \
   HC-SR04 Echo => GPIO 0 On Raspberry Pi Pico \
   HC-SR04 GND(-) => GND(-) On Raspberry Pi Pico
2. Open Thonny on your Raspberry Pi.
3. Create a file named main.py.
4. Copy the [main.py](main.py) file from my GitHub and paste it in the main.py file you have just created.
5. Click the run button in Thonny.
