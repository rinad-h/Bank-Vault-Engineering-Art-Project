import utime

class ButtonHandler:
    """
    Handles button presses with debounce logic.
    """
    def __init__(self, button_pin, debounce_ms=200):
        """
        Initializes the button handler.

        :param button_pin: The GPIO pin the button is connected to.
        :param debounce_ms: The debounce time in milliseconds.
        """
        self.button = button_pin
        self.debounce_ms = debounce_ms
        self.last_press_time = 0
        self.callback = None
        self.button.irq(trigger=self.button.IRQ_FALLING, handler=self._handle_press)

    def _handle_press(self, pin):
        """
        Internal method to handle button press interrupts.

        :param pin: The GPIO pin triggering the interrupt.
        """
        current_time = utime.ticks_ms()
        if utime.ticks_diff(current_time, self.last_press_time) > self.debounce_ms:
            if self.callback:
                self.callback()  # Execute the callback function
        self.last_press_time = current_time

    def set_callback(self, callback):
        """
        Sets the callback function to be executed on button press.

        :param callback: The callback function.
        """
        self.callback = callback
