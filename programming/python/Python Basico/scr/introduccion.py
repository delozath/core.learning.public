import this

print("¡Hola Mundo!")

#Tipos de datos + operaciones básicas
x = 3
type(x)
dir(x)

x = 35 + 20 - 25
print(x)

x = 2*x
print(x)

x = 9
r = x**2
print(f"cuadrado: x^2 = {r}")

x = 3
n = 5
r = x**n
print(f"potencia: {x}^{n} = {r}")


x = 11
#
int_div   = x//2
residuo   = x%2
float_div = x/2
print(f"división entera : {int_div}")
print(f"residuo división: {residuo}")
print(f"división reales : {float_div}")

print(f"""
división entera : {int_div}
residuo división: {residuo}
división reales : {float_div}""")


x = 5.5
type(x)
#ejemplos operaciones

type(int)
type(float)

int(8.489)

x = 9.1278
y = x - int(x)
print(f"Los decimales de {x} son: {y}")

x = 'hola'
x.upper()
y = 'como estás'

x + y + '?'
x + ' ' + y + '?'

print('¿', x, y, '?')
print(f"¿{x} {y}?")

'hola '*3

##combinaciones
'1' + '1'
1 + '1'

#cast
x   = '-2.47'
xf  = float(x)
xi  = int(xf)
xis = str(xi)

xis = str(int(float(x)))

#mejor solucion, pero aun faltan algunos elementos
ix = x.index('.')
x[:ix]

x = True
dir(x)

#operadores
# and or not
#operadores bitwise

x = 10
(x>3) and (x<20)

5 and 3
5 & 3

bin(5)
bin(3)

#complejos
x = 2 + 3j

mag_2 = x.real**2 + x.imag**2

mag_2 = x*x.conjugate()
mag_2 = mag_2.real

import math
dir(math)

math.pi
math.sqrt(mag_2)

mag = math.sqrt(mag_2)
print(f"|x| = {mag}")
#print(f"|x| = {mag:6.4f}")


#entrada estandar
x = input("\n\nIngresa un número: ")
print(f"\n\n\n{x}, {type(x)}")

x = input("\n\nIngresa un número: ")
x = int(x)
print(f"\n\n\n{x}, {type(x)}")

x = input("\n\nIngresa un número: ")
x = float(x)
print(f"\n\n\n{x}, {type(x)}")


#representaciones
bin(75)
hex(60)


#estructuras de control
#condicionales
UMBRAL = 50
x      = 51
if x<UMBRAL:
    print(f'{x} menor que {UMBRAL}')
else:
    print(f'{x} mayor o igual que {UMBRAL}')



UMBRAL = 50
x      = 51
if x==UMBRAL:
    print(f'{x} igual {UMBRAL}')
elif x>UMBRAL:
    print(f'{x} mayor o igual que {UMBRAL}')
else:
    print(f'{x} menor que {UMBRAL}')


#número mayor
x0, x1, x2 = 30, 21, 9
if x0>x1:
    if x0>x2:
        print(f"x0 = {x0} es mayor")
    else:
        print(f"x1 = {x2} es mayor")
else:
    if x1>x2:
        print(f"x1 = {x1} es mayor")
    else:
        print(f"x2 = {x2} es mayor")

#horario tarde, temprano, finde
 
#loops
#lista
lista = [1, 2, 3, 4, 5]

i = 0
print(f"\n lista[{i}] -> {lista[i]}")

#indexing
i = -1
print(f"\n lista[{i}] -> {lista[i]}")
lista[1:]
lista[:-1]
lista[1:-1]
lista[2:-1]
lista[0::2]
lista[1::2]
lista[::-1]

#Class List
x = []
y = list()
type(x)

x.append(10)
x.append(20)
x.append(35)
x.insert(1, -1)


#for
"""
for each:
    i
"""
lista = [1, 2, 3, -1, 'hola ', True]
for l in lista:
    print(f" - {l}")


#Evaluar polinomio

#Fibonacci
items = [2, 3, 4, 5, 6, 7, 8, 9]
fibo  = [1, 1]
for i in items:
    nx = fibo[-1] + fibo[-2]
    fibo.append(nx)

print(fibo)

#range class
dir(range)
i = range(5)
i = list(i)
i = list(range(5))
i = list(range(2, 10))

##
N     = 5
fibo  = [1, 1]
#for i in list(range(2, N+1)):
for i in range(2, N+1):
    nx = fibo[-1] + fibo[-2]
    fibo.append(nx)

print(fibo)

##full fibo
N     = 10
fibo  = []
if N==0:
    fibo = [1]
elif N==1:
    fibo = [1, 1]
elif N>1:
    fibo  = [1, 1]
    for i in range(2, N+1):
        nx = fibo[-1] + fibo[-2]
        fibo.append(nx)
else:
    print('Error N<0')

print(fibo)

##Binario
###version lista
N = 10
n = N
binary = []
#for i in range(8):
for _ in range(8):
    bit = n%2
    n   = n//2
    #
    binary.append(bit)

binary = binary[::-1]
print(binary)

###versión string
N = 10
n = N
binary = ''
#for i in range(8):
for _ in range(8):
    bit = n%2
    n   = n//2
    #
    #binary = binary + str(bit)
    binary += str(bit)

binary = binary[::-1]
print(f"0b{binary}")

###full version
NBITS = 12
#
N = 248
n = N
binary = ''
for i in range(1, NBITS+1):
    bit = n%2
    n   = n//2
    #
    binary += str(bit)
    if i%4==0:
        binary += ' '

if binary[-1] == ' ':
    binary = binary[:-1]

binary = binary[::-1]
print(f"0b{binary}")


#enumerate
lista = ['manzana', 'pera', 'aguacate', 'guayaba', 'fresa']
#
i = 0
for ls in lista:
    i += 1
    print(f"{i}. {ls}")

### iteradores + enumerate + next
dir(enumerate)
it = iter(enumerate(lista))
dir(next)

for i, ls in enumerate(lista):
    print(f"{i+1}. {ls}")

#zip
frutas = ['manzana', 'pera', 'aguacate', 'guayaba', 'naranja']
rasgos = ['verde'  , 'mantequilla', 'hass', 'rosa', 'agria']
#rasgos = ['verde'  , 'mantequilla', 'hass', 'rosa']

for i in range(len(frutas)):
    fruta = frutas[i]
    rasgo = rasgos[i]
    print(f" - {fruta} {rasgo}")

#diferente tamaño

dir(zip)
zip(frutas, rasgos)
it = zip(frutas, rasgos)
next(it)

for fruta, rasgo in zip(frutas, rasgos):
    print(f" - {fruta} {rasgo}")


frutas     = ['manzana', 'pera', 'aguacate', 'guayaba', 'naranja']
rasgos     = ['verde'  , 'mantequilla', 'hass', 'rosa', 'agria']
existencia = [20.938840, 30.2501, 25.55, 2.5698, 38.5545]

for fruta, rasgo, exist in zip(frutas, rasgos, existencia):
    print(f" - {fruta} {rasgo} {exist}")

#enumerate + zip
it = iter(enumerate(zip(frutas, rasgos, existencia)))
next(it)

for i, (fruta, rasgo, exist) in enumerate(zip(frutas, rasgos, existencia)):
    print(f" {i}. {fruta} {rasgo} {exist}")
    #print(f" {i}. {fruta:8s} {rasgo:11} {exist:6.3f}")
    #print(f" {i}. {fruta:8s} {rasgo:11} {exist:06.3f}")

#Burbuja
x = [1, 9, 2, 20, -1, 5]
N = len(x)
#repite proceso
for i in range(1, N):
    if x[i-1]>x[i]:
        x[i-1], x[i] = x[i], x[i-1]

N -= 1
print(x)

###full version
x = [1, 9, 2, 20, -1, 5]
N = len(x)
while N>1:
    for i in range(1, N):
        if x[i-1]>x[i]:
            x[i-1], x[i] = x[i], x[i-1]
    #
    N -= 1
    print(x)


#Estructuras de datos
#listas
x = [0, 1, 2, 3, 4, 5]
x = list(range(6))

x.remove(x[-1])
del(x[2])
x.insert(1, -1)
pop = x.pop()

expr = "((1-2)/(8-4))^2"
expr = "((1-2)/(8-4))^2"

process = expr.replace(' ', '')

syntax = []
for p in process:
    if p=='(':
        syntax.append(p)
    elif p==')':
        if len(syntax)>0:
            _ = syntax.pop()
        else:
            print('Error: sobran )')

if len(syntax)!=0:
    print('Error: sobran (')
else:
    print('Expresión correcta')



process = expr.replace(' ', '')
syntax = []
flag   = True
for p in process:
    if p=='(':
        syntax.append(p)
    elif p==')':
        if len(syntax)>0:
            _ = syntax.pop()
        else:
            print('Error: sobran )')
            flag = False

if flag:
    if (len(syntax)==0):
        print('Expresión correcta')
    else:
        print('Error: sobran (')



expr = "((1-2)/(8-4))^2"

process = expr.replace(' ', '')
syntax = []
for p in process:
    if p=='(':
        syntax.append(p)
    elif p==')':
        if len(syntax)>0:
            _ = syntax.pop()
        else:
            print('Error: sobran )')
            break
else:
    if (len(syntax)==0):
        print('Expresión correcta')
    else:
        print('Error: sobran (')