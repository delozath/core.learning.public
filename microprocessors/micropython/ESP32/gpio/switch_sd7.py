import time

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

class Examen:
    MAX_VALUE = 255
    MAX_TIME = 100
    #
    def __init__(self):
        self.d7s = D7S()
        self.reset = Pin(18, Pin.IN)
        self.list = []
        self.idx = 0
        self.timer = 0
        self.state = 'capture'
        self.min = 2**31
    #
    def s_capture(self):
        x = input("dato: ")
        if x=='t':
            if len(self.list)==0:
                print("Error lista vacia")
            else:
                self.state = 'display'
                self.list.sort(reverse=True)
                self.len = len(self.list)
        elif x.isdigit():
            x = int(x)
            if (x>-1) and (x<256):
                self.min = x if x<self.min else self.min
                self.list.append(x)
            else:
                print("Dato fuera del intervalo [0, 255]")
        else:
            print("Dato negativo o no numerico")
        #
        self.d7s.driver_2display(self.min, 10)
    #
    def s_display(self):
        #
        if self.reset.value()==0:
            self.timer += 1
            if self.timer>Examen.MAX_TIME:
                self.timer = 0
                self.idx += 1
                if self.idx>=self.len:
                    self.idx = 0
            #
            self.d7s.driver_2display(self.list[self.idx], 16)
        else:
            self.state = 'capture'
            self.list = []
            self.len = 0
            self.idx = 0
            self.timer = 0
            self.min = 2**31
            mem32[D7S.GPIO_OUT_REG] = 0
            print("Sistema reiniciado")
    #
    def run(self):
        states = {'capture': self.s_capture,
                  'display': self.s_display}
        #
        while 1:
            func = states[self.state]
            func()
            time.sleep_ms(10)
#
def main():
    exm = Examen()
    exm.run()
#
if __name__ == '__main__':
    main()
    
    
    


