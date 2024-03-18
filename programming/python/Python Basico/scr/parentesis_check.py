#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Analiza una expresión con paréntesis e indica si para cada
paréntesis de apertura existe uno de cierre.

Hay tres implementaciones:
 - analisis_sintaxis_v1: Esta tiene un error en el manejo de las condicionales
 - analisis_sintaxis_v2: Solución funcional con el uso de variables bandera
 - analisis_sintaxis_v3: Solución funcional con la contrucción for-break-else

Ejemplo de uso

Ejemplo:
./parentesis_check.py 
Ingresa expresión a evaluar: (1+3/(5+8))
"""

def main():
    expr = input("Ingresa expresión a evaluar: ")
    expr = expr.replace(' ', '')
    
    stack = []
    analisis_sintaxis_v1(expr, stack)
    #analisis_sintaxis_v2(expr, stack)
    #analisis_sintaxis_v3(expr, stack)

def analisis_sintaxis_v1(expr, stack):
    print("\nVersion 1")
    for e in expr:
        if e=='(':
            stack.append(e)
        elif e==')':
            if len(stack)>0:
                stack.pop()
            else:
                print("Error: extra )")
    #
    if len(stack)==0:
        print("Sintaxis correcta")
    else:
        print("Error: extra (")


def analisis_sintaxis_v2(expr, stack):
    print("\nVersion 2")
    error_flag = False
    for e in expr:
        if e=='(':
            stack.append(e)
        elif e==')':
            if len(stack)>0:
                stack.pop()
            else:
                print("Error: extra )")
                error_flag = True
    #
    if not error_flag:
        if len(stack)==0:
            print("Sintaxis correcta")
        else:
            print("Error: extra (")


def analisis_sintaxis_v3(expr, stack):
    print("\nVersion 3")
    for e in expr:
        if e=='(':
            stack.append(e)
        elif e==')':
            if len(stack)>0:
                stack.pop()
            else:
                print("Error: extra )")
                break
    else:
        if len(stack)==0:
            print("Sintaxis correcta")
        else:
            print("Error: extra (")


if __name__ == '__main__':
    main()
    