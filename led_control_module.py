from machine import Pin

class LEDControl:
    """
    Controls an LED connected to a GPIO pin.
    """
    def __init__(self, pin):
        """
        Initializes the LED control.

        :param pin: The GPIO pin the LED is connected to.
        """
        self.led = Pin(pin, Pin.OUT)

    def toggle(self):
        """
        Toggles the LED state (ON/OFF).
        """
        self.led.value(not self.led.value())
