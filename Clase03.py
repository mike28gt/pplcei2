#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:11:58 2023

@author: miguelcatalan
"""

"""
Expresiones
    * Una combinación de datos, variables y operadores
    * Expresiones aritméticas
"""

print(2 + 3)

resultado_1 = 2 + 3
print(resultado_1)

numero_1 = 3.15

print(numero_1 * 5.5)

resultado_2 = numero_1 * 5.5 
print(resultado_2)

print(numero_1 - numero_1)

resultado_3 = numero_1 - numero_1
print(resultado_3)

print(numero_1 - 2 * 3.25 / numero_1 ** 2)

resultado_4 = numero_1 - 2 * 3.25 / numero_1 ** 2
print(resultado_4)

"""
Precedencia de operadores
    1. Paréntesis
    2. Exponenciación 
    3. Multiplicación y división
    4. Suma y resta
"""

expresion_1 = 3 + 2 - 1

expresion_2 = 3 * 2 / 2
print(expresion_2)

a = 4
b = -12
c = 9
x_1 = (-b + (b**2 - 4*a*c)**1/2) / (2*a)
x_2 = (-b - (b**2 - 4*a*c)**1/2) / (2*a)
print(x_1)
print(x_2)

"""
Operador módulo o residuo
    * Se representa con el símbolo %
    * Este retorna como resultado el residuo de una división
    * Su precedencia en la solución de operaciones es la misma que la división y multiplicación
"""
resultado_5 = 5 % 2
print(resultado_5)

resultado_6 = 7 % 3
print(resultado_6)

resultado_7 = 4 % 2
print(resultado_7)

"""
4 / 2 * 5 % 1
2 * 5 % 1
10 % 1
0
"""

    



