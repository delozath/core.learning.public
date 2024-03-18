import machine as mn
import network
import urequests
import time

import gc
gc.collect()

#https://ifttt.com/ activar un webhook
#https://ifttt.com/my_services --> consultar los servicios que tienen activos --> 
#                              --> ir a la documentación del webhook y copiar al api-key
#lanzar el servicio, podrán publicar hasta 25 tweets al día

topic    = 'topico'
ssid     = 'nombre_red'
password = 'password'
api_key  = 'key'

def isr_gpio(count):
    count[0] += 1
    print(count[0])
    values  = {'value1':count[0]}
    post    = {'Content-Type': 'application/json'}
    #
    request = urequests.post(
        f'https://maker.ifttt.com/trigger/{topic}/with/key/' + api_key,
        json   =values,
        headers=post)
    request.close()
    return 

def config():
    count  = [0]
    button = mn.Pin(0, mn.Pin.IN)
    button.irq(trigger=mn.Pin.IRQ_FALLING, handler=lambda button: isr_gpio(count))
    #
    station = network.WLAN(network.STA_IF)
    #
    station.active(True)
    station.connect(ssid, password)
    #
    while station.isconnected() == False:
        pass
    #
    print('Conexión exitosa')
    print(station.ifconfig())

def main():
    config()
    while 1:
        print('Waiting')
        time.sleep(1)

if __name__ == '__main__':
    main()


