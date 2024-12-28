import time
import machine
from machine import Pin
import utime
from networking import connect
from lcd_display import init_lcd, display_message
from button_control import button_press
from neopixel_control import init_neopixels, set_neopixels
from exchange_rate import get_exchange_rate

# Set up hardware components
sda = machine.Pin(26)
scl = machine.Pin(27)
lcd = init_lcd(sda, scl)  # Initialize the LCD display

# Set up button
button = Pin(1, Pin.IN, Pin.PULL_DOWN)
button.irq(trigger=Pin.IRQ_FALLING, handler=button_press)  # Attach interrupt handler for button press

# Set up neopixels
numpix = 30
pixels = init_neopixels(numpix, 28)  # Initialize NeoPixels with 30 pixels on pin 28

# Connect to Wi-Fi
try:
    connect()  # Attempt to connect to Wi-Fi
except KeyboardInterrupt:
    machine.reset()  # Reset the machine on KeyboardInterrupt
    print('Connected. End of code.')

# Main loop
while True:
    exchange_rate = button_press(button)  # Fetch the exchange rate on button press
    if exchange_rate:  # If exchange rate data is received
        display_message(lcd, exchange_rate)  # Display the exchange rate on the LCD
    time.sleep(1)  # Sleep for 1 second before checking again
