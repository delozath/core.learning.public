from machine import Timer, mem32, Pin

PIN_LED = 22
MAP_LED = (1<<PIN_LED)

GPIO_OUT_REG1 = 0x3FF44004

def toggle(timer):
    mem32[GPIO_OUT_REG1] ^= MAP_LED

def config():
    led = Pin(PIN_LED, mode=Pin.OUT)
    led.value(1)
    #
    timer = Timer(0)
    timer.init(period=500, mode = Timer.PERIODIC, callback=toggle)
    #
    return timer

timer = config()
while 1:
    pass