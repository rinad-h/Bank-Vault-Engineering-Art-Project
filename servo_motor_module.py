from servo import Servo
import time

class ServoMotor:
    """
    Controls a servo motor.
    """
    def __init__(self, pin):
        """
        Initializes the servo motor.

        :param pin: The GPIO pin the servo is connected to.
        """
        self.servo = Servo(pin=pin)

    def rotate(self):
        """
        Rotates the servo between 0 and 90 degrees with delays.
        """
        self.servo.move(0)  # Move to 0 degrees
        time.sleep(1)
        self.servo.move(90)  # Move to 90 degrees
