# Simple RGB LED:
Schematic - See below the schematic for instructions:
 
![](Schematic.png)
 
What You Will Need:
- 1 x Raspberry Pi Pico
- 1 x Breadboard
- 1 x RGB LED
- 15 x Jumper Wires
- 3 x 220Ω Resistors
- 3 x Potentiometers

Setting Up The Circuit:
1. Make the circuit: \
   Raspberry Pi Pico GND(-) => Negative Power Rail
   Raspberry Pi Pico 3.3v => Positive Power Rail
   RGB LED Pin 1 => 220Ω Resistor => GPIO 0 \
   RGB LED Pin 2 => 3.3v On Raspberry Pi Pico \
   RGB LED Pin 3 => 220Ω Resistor => GPIO 1 \
   RGB LED Pin 4 => 220Ω Resistor => GPIO 2 \
   Potentiometer 1 Pin 1 => Negative Power Rail \
   Potentiometer 1 Pin 2 => GPIO 28 On Raspberry Pi Pico \
   Potentiometer 1 Pin 3 => Positive Power Rail \
   Potentiometer 2 Pin 1 => Negative Power Rail \
   Potentiometer 2 Pin 2 => GPIO 27 On Raspberry Pi Pico \
   Potentiometer 2 Pin 3 => Positive Power Rail \
   Potentiometer 3 Pin 1 => Negative Power Rail \
   Potentiometer 3 Pin 2 => GPIO 26 On Raspberry Pi Pico \
   Potentiometer 3 Pin 3 => Positive Power Rail
2. Open Thonny on your Raspberry Pi.
3. Create a file named main.py.
4. Copy the [main.py](main.py) file from my GitHub and paste it in the main.py file you have just created.
5. Click the run button in Thonny.
6. Rotate the first potentiometer to change the brightness of the red, rotate the second potentiometer to change the brightness of the green, rotate the third potentiometer to change the brightness of the blue.