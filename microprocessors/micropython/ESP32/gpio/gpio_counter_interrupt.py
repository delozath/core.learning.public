import time
import machine

from micropython import const
from machine import mem32, Pin

class D7S:
    GPIO_ENABLE_REG = const(0x3FF44020)
    GPIO_OUT_REG = const(0x3FF44004)
    #
    def __init__(self):
        A = 1<<4
        B = 1<<15
        C = 1<<19
        D = 1<<22
        E = 1<<23
        F = 1<<16
        G = 1<<17
        #
        DS0 = 5 #display selector
        DS1 = 21
        #
        mem32[D7S.GPIO_ENABLE_REG] = A + B + C + D + E + F + G + (1<<DS0) + (1<<DS1)
        #
        numbers = {0 : ~(A + B + C + D + E + F),
                   1 : ~(B + C),
                   2 : ~(A + B + D + E + G),
                   3 : ~(A + B + C + D + G),
                   4 : ~(B + C + F + G),
                   5 : ~(A + C + D + F + G),
                   6 : ~(A + C + D + E + F + G),
                   7 : ~(A + B + C),
                   8 : ~(A + B + C + D + E + F + G),
                   9 : ~(A + B + C + F + G),
                   10: ~(A + B + C + E + F + G),
                   11: ~(C + D + E + F + G),
                   12: ~(A + D + E + F),
                   13: ~(B + C + D + E + G),
                   14: ~(A + D + E + F + G),
                   15: ~(A + E + F + G),
                   'clear': (A + B + C + D + E + F + G)}
        #
        self.numbers = numbers
        #
        self.select_0 = Pin(DS0, Pin.OUT)
        self.select_1 = Pin(DS1, Pin.OUT)
        self.select_0.on()
        self.select_1.on()
        #
        self.DS0 = (1<<DS0)
        self.DS1 = (1<<DS1)
        #
        self.selector = 0
        mem32[D7S.GPIO_OUT_REG] = 0
    #
    def driver_2display(self, num, base=10):
        digit_0  = num % base
        digit_1 = num // base
        #
        if self.selector==0:
            self._show_2seg(digit_0, 0)
            self.selector += 1
        else:
            self._show_2seg(digit_1, 1)
            self.selector = 0
    #
    def _show_2seg(self, num, sel):
        if sel==0:
            mem32[D7S.GPIO_OUT_REG] = self.numbers.get(num, 0)
            self.select_0.on()
            self.select_1.off()
        elif sel==1:
            mem32[D7S.GPIO_OUT_REG] = self.numbers.get(num, 0)
            self.select_1.on()
            self.select_0.off()
        else:
            self.select_1.off()
            self.select_0.off()

class GPIO_driver:
    MAX_VALUE = 10
    MAX_TIME = 100
    #
    def __init__(self, button):
        self.button = button
        self.button.irq(trigger=Pin.IRQ_RISING, handler=self.button_isr)
        self.state = 'event'
        self.timer = 0
        self.count = 0
    #
    def button_isr(self, pin):
        self.button.irq(trigger=0, handler=self.button_isr)
        self.count += 1
        self.state = 'block'
    #
    def s_event(self):
        pass
    #
    def s_wait(self):
        self.timer += 1
        if self.timer>GPIO_driver.MAX_TIME:
            self.timer = 0
            self.state = 'event'
            self.button.irq(trigger=Pin.IRQ_RISING, handler=self.button_isr)
        print(f"timer: {self.timer}")
            
    #
    def run(self):
        states = {'block': self.s_wait,
                  'event': self.s_event}
        #
        display = D7S()
        while 1:
            func = states[self.state]
            func()
            display.driver_2display(self.count, 10)
            print(f"count: {self.count}")
            time.sleep_ms(10)
#
def main():
    pin = Pin(18, mode=Pin.IN, pull=Pin.PULL_DOWN)
    gpio_intr = GPIO_driver(pin)
    gpio_intr.run()
#
if __name__ == '__main__':
    main()
    
    
    


