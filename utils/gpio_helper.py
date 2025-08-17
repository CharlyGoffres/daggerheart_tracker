# utils/gpio_helper.py
"""
GPIOHelper abstracts GPIO access. Uses RPi.GPIO if available, else mocks for development.
"""
try:
    import RPi.GPIO as GPIO
    RPI = True
except ImportError:
    RPI = False

class GPIOHelper:
    def __init__(self):
        if RPI:
            GPIO.setmode(GPIO.BCM)
        self.pins = [17, 18, 27]  # Example pins

    def read_all(self):
        if RPI:
            return {pin: GPIO.input(pin) for pin in self.pins}
        else:
            # Mocked data for development
            return {pin: 0 for pin in self.pins}
