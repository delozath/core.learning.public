# Introducción a MicroPython en ESP32: Blink (Parpadeo) de un LED

MicroPython es una implementación ligera del lenguaje de programación Python, es decir, es una versión más pequeña y optimizada para ser implementada en microcontroladores de recursos limitados. En este folder, aprenderemos a los elementos básicos de un programa MicroPython pensados para la placa de desarrollo ESP32, haciendo parpadear un LED conectado a uno de sus pines *General Purpose Input/Output* (GPIO).


## Requisitos Previos
<details>

Antes de comenzar, asegúrate de tener lo siguiente:
- Una placa de desarrollo ESP32.
- Firmware de MicroPython instalado en tu ESP32. Puedes descargar la última versión desde [MicroPython Downloads](https://micropython.org/download/ESP32_GENERIC/).
- Thonny IDE instalado en tu computadora. Puedes descargarlo desde [Thonny.org](https://thonny.org/).
- Si usas Windows o macOS, instala los drivers del [bridge USB a Serial](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers). 
- Conexión USB para comunicarte con la placa ESP32. 
- El repositorio oficial con todas las fuentes de MicroPython lo puedes encontrar en [MicroPython ESP32](https://github.com/micropython/micropython).

Las siguientes secciones asumirán que ya tienes todo lo anterior listo y funcionando.

</details>



## Estructura del Programa Blink en MicroPython

<details>

### Implementación con enfoque de programación estructurada no optimizado

**Blink Básico**

[🔗 link al archivo completo](./blink_prog_estruct.py)
El programa para hacer parpadear un LED en MicroPython consiste en:


1. **Importar Módulos**: 
`machine`: esta es núcleo de implementación de MicroPython que permite interactuar con el Hardware del ESP32. A través de esta biblioteca se puede acceder a los dispositivos periféricos como son GPIO, SPI, I2C, ADC, DAC, etc.
`time`: es una subimplementación del módulo estándar de Python que proporciona funciones relacionadas con la gestión del tiempo, solo que en lugar de estar enlazada a un sistema operativo completo, está adaptada para microcontroladores, ofreciendo funciones básicas como pausas y mediciones de tiempo.
`Pin`: es una *clase* dentro del módulo `machine` que permite configurar y controlar los pines GPIO del ESP32.

```python
import time
from machine import Pin
```

2. **Configurar el Pin del LED**:
Se crea una instancia del pin GPIO al que va a conectar el LED. En este caso, se utiliza el pin 25, configurado como salida.

En este caso `Pin.IN` y `Pin.OUT` representan constantes que indican la dirección del pin, es decir, si se va a usar para entrada (leer datos) o salida (enviar datos). Debido a que diversos protocolos se representan con mayúsculas en MicroPython, a veces la convención del uso de mayúsculas para indicar constantes puede ser confusa, con respecto a la implementación estándar de Python.


```python
led = Pin(25, Pin.OUT)
```

3. **Loop Infinito**:
A diferencia de los programas convencionales de Python que terminan su ejecución después de completar todas las instrucciones, en el diseño de programas para dispositivos embebidos o de propósito específico basados en microcontroladores sin sistema operativo; es común utilizar un loop infinito para mantener el programa en ejecución continua, ya que se asume que el dispositivo debe estar siempre activo, realizando la función para la que fue diseñado. Ejemplos de esto incluyen sistemas de monitoreo en tiempo real, señalizaciones, máquinas expendedoras, entre otros. En resumen, el uso de un loop infinito es una práctica estándar en la programación de microcontroladores, para mantenerlos en funcionamiento continuo.

Posteriormente, se revisará que esta condición de un loop infinito puede mapearse a una abstracción de sistemas conocido como **Automatas Finito** o también **Máquina de Estados Finitos** (FSM por sus siglas en inglés), que es un modelo matemático utilizado para diseñar sistemas lógicos y de control.

En este caso particular el ciclo infinito se define como `while True:` o su equivalente `while 1:`

La secuencia del parpadeo a una frecuencia de 1 Hz, corresponde a:
1. encender el LED --> valor del pin a `1`
2. esperar medio segundo --> `time.sleep(0.5)`
3. apagar el LED --> valor del pin a `0`
4. esperar medio segundo --> `time.sleep(0.5)`

En este ejemplo se incluye la impresión en consola (*REPL* Read-Eval-Print Loop) del estado del LED

```python
while True:
    led.value(1)
    print("Led encendido")
    time.sleep(0.5)
    
    led.value(0)
    print("Led apagado")
    time.sleep(0.5)
```
</details>

------

## REPL: Interacción con el MicroPython

<details>

El REPL (Read-Eval-Print Loop) es un entorno interactivo que permite a los usuarios escribir y ejecutar código de MicroPython línea por línea. Los IDE de desarrollo como Thonny, tienen una implementación integrada donde se puede acceder al REPL de MicroPython.

Es importante destacar que el REPL es una ventana de comando tipo CLI (Command Line Interface) la cual permite ejecutar comandos en el interprete de MicroPython y observar los resultados en dicha ventada de comandos. En otras palabras, desde la ventana del REPL se envían los comandos al interprete de MicroPython que se encuentra corriendo en el ESP32, mismo que ejecuta los comandos y devuelve los resultados que son mostrados en la ventana del REPL. Todo el envío y recepción se realiza a través de la conexión serial USB entre la computadora y bridge USB-Serial del ESP32.

</details>

## Optimización del Blink

### Blink Optimizado con un solo sleep

Esta optimización utiliza la función XOR para generar el cambio de encendido a apagado, y viceversa

a XOR 1 = not a

x = 0b0000_0001

x = x XOR 1

x = 

```text
0b0000_0001
0b0000_0001
-----------
0b0000_0000
```

x = 

```text
0b0000_0000
0b0000_0001
-----------
0b0000_0001
```


[🔗 link al archivo completo](./blink_prog_estruct_xor.py)
El programa para hacer parpadear un LED en MicroPython consiste en:

Blink optimizado con operación binaria XOR

```python
x = 1

while True:
    x ^= 1
    led.value(x)
    time.sleep(0.5)
```
