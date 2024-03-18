import time
#
from machine import Pin
#
led_0 = Pin(25, Pin.OUT)
led_1 = Pin(33, Pin.OUT)
#
while True:
    led_0.value(1)
    led_1.value(1)
    time.sleep(0.5)
    #
    led_0.value(1)
    led_1.value(1)
    time.sleep(0.5)