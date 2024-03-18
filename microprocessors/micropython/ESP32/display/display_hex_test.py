from micropython import const
from machine import mem32, Pin

GPIO_OUT_REG = const(0x3FF44004)

A = 4
B = 15
C = 19
D = 22
E = 23
G = 17
F = 16

DC0 = 5
DC1 = 21

common0 = Pin(DC0, Pin.OUT)
common1 = Pin(DC1, Pin.OUT)
seg_A = Pin(A, Pin.OUT)
seg_B = Pin(B, Pin.OUT)
seg_C = Pin(C, Pin.OUT)
seg_D = Pin(D, Pin.OUT)
seg_E = Pin(E, Pin.OUT)
seg_G = Pin(G, Pin.OUT)
seg_F = Pin(F, Pin.OUT)

DC0 = 1<<DC0
DC1 = 1<<DC1
#
A = 1<<A
B = 1<<B
C = 1<<C
D = 1<<D
E = 1<<E
F = 1<<F
G = 1<<G

CERO = ~(A + B + C + D + E + F)
UNO = ~(B + C)
DOS = ~(A + B + D + E + G)
TRES = ~(A + B + C + D + G)
CUATRO = ~(B + C + F + G)
CINCO = ~(A + C + D + F + G)
SEIS = ~(A + C + D + E + F + G)
SIETE = ~(A + B + C)
OCHO = ~(A + B + C + D + E + F + G)
NUEVE = ~(A + B + C + F + G)
HEX_A = ~(A + B + C + E + F + G)
HEX_B = ~(C + D + E + F + G)
HEX_C = ~(A + D + E + F)
HEX_D = ~(B + C + D + E + G)
HEX_E = ~(A + D + E + F + G)
HEX_F = ~(A + E + F + G)

CLEAR = (A + B + C + D + E + F + G)
DC    = DC0 + DC1

GPIO_MASK = CLEAR | DC

mem32[GPIO_OUT_REG] = OCHO



