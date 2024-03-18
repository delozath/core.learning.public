import machine
import time

SD7 = {
      'all': 0xe007004
      0: 0xe005004
      1: 0x8000004
      2: 0xe006000
      3: 0xa006004
      4: 0x8003004
      5: 0x2007004
      6: 0x6007004
      7: 0x8004004
      8: 0xe007004
      9: 0xa007004
}

GPIO_OUT_REG1 = 0x3FF44004

A, B, C, D, E, F, G = 14, 27, 2, 25, 26, 12, 13

pins = [machine.Pin(i, machine.Pin.OUT) for i in [A, B, C, D, E, F, G] ]



TICK_MS    = 100
N_TICK_SEG = 1000//TICK_MS



state   = 'RESET'
count   = 9
c_ticks = 0
while 1:
    if state=='RESET':
        count = 9
        state = 'COUNT'
    #
    elif state=='COUNT':
        machine.mem32[GPIO_OUT_REG1] = SD7[count]
        c_ticks = 0
        #
        count  -= 1
        state = 'WAIT'
        print(f"state count, count: {count}")
    #
    elif state=='WAIT':
        if c_ticks>N_TICK_SEG:
            if count>-1:
                state ='COUNT'
            else:
                state = 'RESET'
        #
        print(f"state wait, c_ticks: {c_ticks}")
        c_ticks += 1
    #
    time.sleep_ms(TICK_MS)