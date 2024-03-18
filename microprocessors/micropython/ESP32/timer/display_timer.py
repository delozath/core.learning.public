import time
import machine

from micropython import const
from machine import mem32, Pin, Timer

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
#
class Display_Timer():
    MAX_VALUE = 10
    def __init__(self):
        self.display = D7S()
        self.count = 0
        #
        timer_0 = Timer(0)
        timer_0.init(mode=Timer.PERIODIC, period=1000, callback=self._isr_timer_0)        
        #
        timer_1 = Timer(1)
        timer_1.init(mode=Timer.PERIODIC, period=10, callback=self._isr_timer_1)
    #
    def _isr_timer_0(self, timer):
        self.count += 1
    #
    def _isr_timer_1(self, timer):
        self.display.driver_2display(self.count, 10)
    #
    def run(self):
        while 1:
            if self.count>Display_Timer.MAX_VALUE:
                self.count = 0

#
def main():
    disp_timer = Display_Timer()
    disp_timer.run()
#
if __name__ == '__main__':
    main()
    
    
    


