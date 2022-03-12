# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# The number of NeoPixels
num_pixels = 144
# Pin the LED_Strip is connected
pixel_pin = board.D18

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

# Code
brightness = 255



pixels[0] = (255, 0, 0)  # Red
time.sleep(2)
pixels[2] = (0, 255, 0)  # Green

time.sleep(5)

pixels[2] = (0, 0, 0)
time.sleep(1)
pixels[0] = (0, 0, 0)

time.sleep(5)