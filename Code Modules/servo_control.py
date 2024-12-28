from machine import Pin, PWM

class Servo:
    def __init__(self, pin):
        """
        Initialize the servo motor.
        Args:
            pin: The pin to which the servo is connected
        """
        self.servo_pin = Pin(pin, Pin.OUT)  # Create a pin object for the servo motor
        self.pwm = PWM(self.servo_pin)  # Create a PWM object for controlling the servo
        self.pwm.freq(50)  # Set PWM frequency to 50Hz for servo motors
    
    def move(self, angle):
        """
        Move the servo to a specified angle.
        Args:
            angle: The target angle for the servo (0-180 degrees)
        """
        pulse_width = 500 + (angle * 1000 // 180)  # Calculate the pulse width for the desired angle
        self.pwm.duty_u16(pulse_width)  # Set the PWM duty cycle to control the servo
