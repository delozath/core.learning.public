import uasyncio

from machine import Pin, I2C

async def blink(led, T):
    while True:
        led.on()
        await uasyncio.sleep_ms(T)
        led.off()
        await uasyncio.sleep_ms(T)

async def receive(i2c):
    while 1:
        x = i2c.readfrom(50, 1)
        print(x)
        await uasyncio.sleep_ms(1000)

def main():
    pin_1 = Pin(12, Pin.OUT)
    pin_2 = Pin(14, Pin.OUT)
    i2c   = I2C(1, scl=Pin(23), sda=Pin(22), freq=400000)
    #
    loop = uasyncio.get_event_loop()
    loop.create_task(blink(pin_1, 45))
    loop.create_task(blink(pin_2, 56))
    loop.create_task(receive(i2c))
    #
    loop.run_forever()

if __name__ == '__main__':
    main()