#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    n = input('¿Cuántos valores de la serie de Fibonacci quieres que se muestren?:\n')
    if n.isnumeric():
        n    = int(n)
        #fibo = fibonacci(n)
        fibo = [1]
        fibonacci_ref(n, fibo)
        print('Fibonacci:', fibo, '\n'*2)
    else:
        print("\n Error: el dato ingresado debe ser entero positivo")
        
def fibonacci(n):
    fn = [1, 1]
    if n>1:
        for _ in range(2, n+1):
            f = fn[-1] + fn[-2]
            fn.append(f)
        return fn
    elif n==1:
        return fn
    elif n==0:
        return fn[0:1]

def fibonacci_ref(n, fn):
    if n>1:
        fn.append(1)
        for _ in range(2, n+1):
            f = fn[-1] + fn[-2]
            fn.append(f)
    elif n==1:
        fn.append(1)

if __name__ == '__main__':
    main()