import machine

from machine import Timer

#
class Timer_Driver():
    MAX_VALUE = 10
    def __init__(self):
        self.count = 0
        #
        timer_0 = Timer(0)
        timer_0.init(mode=Timer.PERIODIC, period=1000, callback=self._isr_timer_0)        
    #
    def _isr_timer_0(self, timer):
        self.count += 1
        print(self.count)
    #
    def run(self):
        while 1:
            if self.count>Timer_Driver.MAX_VALUE - 1:
                self.count = 0

#
def main():
    timer = Timer_Driver()
    timer.run()
#
if __name__ == '__main__':
    main()
    
    
    


