from machine import Pin, I2C

i2c = I2C(1, scl=Pin(23), sda=Pin(22), freq=400000)

i2c.scan()

i2c.readfrom(32, 1)
i2c.readfrom(32, 10)