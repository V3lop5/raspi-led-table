# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# The number of NeoPixels
from matrix import Matrix

num_pixels = 30 * 30
# Pin the LED_Strip is connected
pixel_pin = board.D18

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)


def update_led_matrix(matrix: Matrix):
    counter = 0
    while counter < num_pixels:
        pixels[counter] = matrix.pixel[counter].value
        counter = counter + 1
