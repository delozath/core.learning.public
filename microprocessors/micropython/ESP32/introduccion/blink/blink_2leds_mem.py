import time

from machine import Pin, mem32

GPIO_OUT_REG = 0x3FF44004
PIN_0        = 25
PIN_1        = 26

led_0 = Pin(PIN_0, Pin.OUT)
led_1 = Pin(PIN_1, Pin.OUT)

mem32[GPIO_OUT_REG] = (1<<PIN_0) | (1<<PIN_1)
time.sleep(2)
while True:
    time.sleep(0.5)
    mem32[GPIO_OUT_REG] ^= (1<<PIN_0) | (1<<PIN_1)
    print("Blinking")
