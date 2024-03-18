from machine import Pin

common0 = Pin(5, Pin.OUT)
common1 = Pin(21, Pin.OUT)

A = 4
B = 15
C = 19
D = 22
E = 23
G = 17
F = 16

seg_A = Pin(A, Pin.OUT)
seg_B = Pin(B, Pin.OUT)
seg_C = Pin(C, Pin.OUT)
seg_D = Pin(D, Pin.OUT)
seg_E = Pin(E, Pin.OUT)
seg_G = Pin(G, Pin.OUT)
seg_F = Pin(F, Pin.OUT)

common0.on()
common1.on()

seg_A.off()
seg_B.off()
seg_C.off()
seg_D.off()
seg_E.off()
seg_G.off()
seg_F.off()

A = 1<<A
B = 1<<B
C = 1<<C
D = 1<<D
E = 1<<E
G = 1<<G
F = 1<<F