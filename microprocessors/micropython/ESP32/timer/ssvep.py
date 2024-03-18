from machine import Timer, mem32, Pin

PIN_LED_7HZ  = 22
PIN_LED_11HZ = 23
#
MAP_LED_7HZ  = (1<<PIN_LED_7HZ)
MAP_LED_11HZ = (1<<PIN_LED_11HZ)

GPIO_OUT_REG1 = 0x3FF44004

def toggle_7hz(timer):
    mem32[GPIO_OUT_REG1] ^= MAP_LED_7HZ

def toggle_11hz(timer):
    mem32[GPIO_OUT_REG1] ^= MAP_LED_11HZ

def config():
    led_7hz  = Pin(PIN_LED_7HZ , mode=Pin.OUT)
    led_11hz = Pin(PIN_LED_11HZ, mode=Pin.OUT)
    #
    led_7hz .value(1)
    led_11hz.value(1)
    #
    timer_7hz = Timer(0)
    timer_7hz.init(period=71, mode=Timer.PERIODIC, callback=toggle_7hz)
    #
    timer_11hz = Timer(1)
    timer_11hz.init(period=45, mode=Timer.PERIODIC, callback=toggle_11hz)    
    #
    #return timer

config()
while 1:
    pass