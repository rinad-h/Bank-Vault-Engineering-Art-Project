import time
from machine import Pin
from button_handler_module import ButtonHandler
from led_control_module import LEDControl
from lcd_display_module import LCDDisplay
from servo_motor_module import ServoMotor
from api_handler_module import APIHandler

# Initialize components
led = LEDControl(pin=0)  # LED control on pin 0
servo = ServoMotor(pin=5)  # Servo motor on pin 5
lcd = LCDDisplay(sda_pin=26, scl_pin=27)  # LCD with SDA on pin 26 and SCL on pin 27
api = APIHandler("https://v6.exchangerate-api.com/v6/3caccaae69d659b02629d974/latest/CAD")  # API for exchange rates

# Configure button input
button = Pin(1, Pin.IN, Pin.PULL_DOWN)
button_handler = ButtonHandler(button, debounce_ms=200)  # Button handler with 200ms debounce

# Define button press callback function
def on_button_press():
    """
    Executes when the button is pressed.
    Rotates the servo, toggles the LED, and displays a random exchange rate.
    """
    servo.rotate()  # Rotate the servo
    led.toggle()  # Toggle the LED state
    rate = api.get_random_conversion_rate()  # Fetch a random exchange rate
    lcd.display_message(rate)  # Display the rate on the LCD

# Set the button press callback
button_handler.set_callback(on_button_press)

# Keep the program running
while True:
    time.sleep(1)
