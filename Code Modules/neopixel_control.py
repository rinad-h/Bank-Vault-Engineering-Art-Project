from neopixel import Neopixel

def init_neopixels(num_pixels, pin, brightness=50):
    """
    Initialize the NeoPixels.
    Args:
        num_pixels: The number of pixels to initialize
        pin: The pin to which the NeoPixels are connected
        brightness: The brightness level (0-255)
    Returns:
        pixels: The initialized NeoPixel object
    """
    pixels = Neopixel(num_pixels, 0, pin, "GRB")  # Create a NeoPixel object with RGB color order
    pixels.brightness(brightness)  # Set the brightness of the pixels
    return pixels

def set_neopixels(pixels, color):
    """
    Set the color of all NeoPixels.
    Args:
        pixels: The NeoPixel object
        color: The color to set (as a tuple of RGB values)
    """
    pixels.fill(color)  # Set the color of all pixels
    pixels.show()  # Update the pixels to show the new color
