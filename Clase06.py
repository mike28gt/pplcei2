#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:39:59 2023

@author: miguelcatalan
"""

"""
Expresiones booleanas
    * Expresiones que van a dar como resultado un tipo de dato booleano.
    * El resultado de estas expresiones solamente puede True o False.
    * Estas expresiones utilizan operadores de comparación.
    * Los operadores de comparación (operadores racionales) son:
        * ==       igual que
        * !=       diferente que
        * >        mayor que
        * <        menor que
        * >=       mayor o igual que
        * <=       menor o igual que
        
"""
print(8 > 7)
print(1 > 7)
print(7 > 7)

resultado_1 = 8 > 7
print("El valor de resultado_1 es: " + str(resultado_1))

numero_1 = 8
numero_2 = 7
resultado_2 = numero_1 > numero_2
print("El valor de resultado_2 es: " + str(resultado_2))

numero_3 = 8
resultado_3 = numero_3 > 5
print("El valor de resultado_3 es: " + str(resultado_3))

print(8 < 7)
print(1 < 7)
print(7 < 7)

print(8 >= 7)
print(1 >= 7)
print(7 >= 7)

print(8 <= 7)
print(1 <= 7)
print(7 <= 7)

print(8 == 7)
print(1 == 7)
print(7 == 7)

print(8 != 7)
print(1 != 7)
print(7 != 7)

"""
Operadores Lógicos
    * Los operadores lógicos utilizan como operandos datos boolean
    * Estos operadores utilizan como operando los valores True y False exclusivamente.
    * Las expresiones lógicas dan como resultado un tipo de dato boolean
    * Los operadores lógicos son:
        * and               y
        * or                o
        * not               no / negación
    * Nota: Python reconoce el tipo de dato int 0 como False y cualquier otro valor como True
"""
print ("True and True: " + str(True and True))
print ("True and False: " + str(True and False))
print ("False and True: " + str(False and True))
print ("False and False: " + str(False and False))

print ("True or True: " + str(True or True))
print ("True or False: " + str(True or False))
print ("False or True: " + str(False or True))
print ("False or False: " + str(False or False))

print ("not(True): " + str(not(True)))
print ("not(False): " + str(not(False)))

print ("not(1): " + str(not(1)))
print ("not(0): " + str(not(0)))


x = 9
resultado_4 = x > 0 and x < 10
#              True and True 
#               True
print("El resultado de resultado_4 es: " + str(resultado_4))



