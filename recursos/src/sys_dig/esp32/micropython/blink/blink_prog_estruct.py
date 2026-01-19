import time
from machine import Pin

led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    print("Led encendido")
    time.sleep(0.5)
    
    led.value(0)
    print("Led apagado")
    time.sleep(0.5)