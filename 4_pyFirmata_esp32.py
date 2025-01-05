# ---------------------------------------------------------------------------- #
#                             PyFirmata ESP32 Test                             #
# ---------------------------------------------------------------------------- #

import pyfirmata2 as pyfirmata
import time

# Set the port where the ESP32 is connected
# board = pyfirmata.Arduino('COM13')  # Change 'COM4' to your port
board = pyfirmata.ESP32('COM13')  # Change 'COM4' to your port

# Start the iterator to prevent buffer overflow
it = pyfirmata.util.Iterator(board)
it.start()

# Define the pin where the LED is connected
led_pin = board.get_pin('d:2:o')  # Digital pin 4 as output

time.sleep(2)  # Wait for setup

while True:
    print("Turn LED on")
    led_pin.write(1)  # Turn on LED
    time.sleep(2)     # Wait for 2 seconds
    
    print("Turn LED off")
    led_pin.write(0)  # Turn off LED
    time.sleep(2)     # Wait for 2 seconds

# ------------------------------------ END ----------------------------------- #
