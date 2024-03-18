import time
import machine

from micropython import const
from machine import mem32, Pin

class GPIO_driver:
    def __init__(self, button):
        self.count = 0
        self.button = button
        self.button.irq(trigger=Pin.IRQ_RISING, handler=self.__button_isr)
    #
    def __button_isr(self, pin):
        self.count = 0       
    #
    def run(self):
        while 1:
            print(f"cuenta: {self.count}")
            self.count +=1
            time.sleep_ms(1000)
#
def main():
    pin = Pin(18, mode=Pin.IN, pull=Pin.PULL_DOWN)
    gpio_intr = GPIO_driver(pin)
    gpio_intr.run()
#
if __name__ == '__main__':
    main()
    
    
    


