import time
from machine import Pin

led = Pin(25, Pin.OUT)
x = 1

while True:
    x ^= 1
    led.value(x)
    time.sleep(0.5)