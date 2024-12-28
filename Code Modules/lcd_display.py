from machine import I2C
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 0x27  # LCD I2C address
I2C_NUM_ROWS = 2  # Number of rows in the LCD
I2C_NUM_COLS = 16  # Number of columns in the LCD

def init_lcd(sda, scl):
    """
    Initialize the I2C LCD display.
    Args:
        sda: Pin for data line
        scl: Pin for clock line
    Returns:
        lcd: The initialized LCD object
    """
    i2c = I2C(1, sda=sda, scl=scl, freq=400000)  # Create an I2C object on controller 1
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)  # Initialize LCD with I2C interface
    return lcd

def display_message(lcd, message):
    """
    Display a message on the LCD screen.
    Args:
        lcd: The LCD object to display the message on
        message: The message string to display
    """
    lcd.clear()  # Clear the display
    lcd.putstr(message)  # Write the message to the display
