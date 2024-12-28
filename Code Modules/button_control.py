import utime
from machine import Pin
from servo import Servo
import urequests
import random

# Button setup with pull-down resistor
button = Pin(1, Pin.IN, Pin.PULL_DOWN)
sg90_servo = Servo(pin=5)  # Initialize servo motor at pin 5
button_presses = 0  # Counter for button presses
last_press_time = 0  # Timestamp of the last button press

def button_press(pin):
    """
    Handles the button press event, controls servo motor, fetches exchange rates,
    and displays the rate on the LCD screen.
    Args:
        pin: The pin that triggered the interrupt (the button pin)
    """
    global button_presses, last_press_time, res  # Access global variables
    current_time = utime.ticks_ms()  # Get the current timestamp
    if utime.ticks_diff(current_time, last_press_time) > 200:  # Debounce: Only trigger after 200ms
        sg90_servo.move(0)  # Move servo to position 0 degrees
        utime.sleep(1)  # Wait for 1 second
        sg90_servo.move(90)  # Move servo to 90 degrees
        utime.sleep(0.5)  # Wait for 0.5 seconds
        led.toggle()  # Toggle LED state (on/off)
        utime.sleep(1)  # Wait for 1 second
        
        button_presses += 1  # Increment the button press counter
        r = urequests.get("https://v6.exchangerate-api.com/v6/3caccaae69d659b02629d974/latest/CAD")
        conversion_rates = r.json().get('conversion_rates', {})  # Get conversion rates from the API
        res = random.choice(list(conversion_rates.items()))  # Randomly select an exchange rate
        
        exchange_rate = str(res)  # Convert the selected exchange rate to a string
        return exchange_rate  # Return the exchange rate to be displayed on the LCD

    last_press_time = current_time  # Update the last press timestamp
    utime.sleep_ms(1)  # Sleep for 1ms to avoid unnecessary CPU usage
