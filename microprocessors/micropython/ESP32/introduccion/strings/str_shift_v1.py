#!/usr/bin/python3
# -*- coding: utf-8 -*-

x = "Hola mundo      "

lx = len(x)
for i in range(lx):
    idx = lx-i-1
    out = x[idx]
    #
    x = x[0:idx] + '_' + x[idx+1:lx]
    
    print("shift char: %c"%out)
    print("remain str: %s\n"%x)
