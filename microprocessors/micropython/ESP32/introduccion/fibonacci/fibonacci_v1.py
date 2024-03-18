#!/usr/bin/python3
# -*- coding: utf-8 -*-

n = input("valor de n:  ")
n = int(n)

fib = [1, 1]
for n in range(2, n+1):
    tmp = fib[n-1] + fib[n-2]
    fib.append(tmp)

for i in range(len(fib)):
    print("%d"%fib[i])