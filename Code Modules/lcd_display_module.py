 from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

class LCDDisplay:
    """
    Handles a 16x2 I2C LCD display.
    """
    I2C_ADDR = 0x27  # I2C address of the LCD
    I2C_NUM_ROWS = 2  # Number of rows on the LCD
    I2C_NUM_COLS = 16  # Number of columns on the LCD

    def __init__(self, sda_pin, scl_pin):
        """
        Initializes the LCD display.

        :param sda_pin: GPIO pin for SDA.
        :param scl_pin: GPIO pin for SCL.
        """
        i2c = I2C(1, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=400000)
        self.lcd = I2cLcd(i2c, self.I2C_ADDR, self.I2C_NUM_ROWS, self.I2C_NUM_COLS)

    def display_message(self, message):
        """
        Displays a message on the LCD.

        :param message: The message to display.
        """
        self.lcd.clear()  # Clear the LCD screen
        self.lcd.putstr(message[:self.I2C_NUM_COLS])  # Display the message (truncate if needed)
