#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:39:00 2023

@author: miguelcatalan
"""

"""
    Estructuras condicionales
    * Estas estructuras permiten ejecutar bloques de código cucando se cumpla cierta condición
"""
if (True):
    print("El valor de la expresión es True")

if (False):
    print("El valor de la expresión es False")
    

x = -1
if (x > 0):
    print("El valor es positivo.")


if (x > 0):
    pass

"""
Ejecución alternativa
"""
x = -1
if (x > 0):
    print("El valor es positivo.")
else:
    print("El valor es negativo.")
    

# Utilizando el operador módulo (%), si el residuo de la división de 
# un número entre 2 es 0, entonces el número es par, de lo contrario
# es impar
x = 325
if (x % 2 == 0):
    print("El número es par.")
else:
    print("El número es impar.")
    
"""
Condicionales encadenados
"""
x = 4
y = 2
#Evaluar si x > y
if (x > y):
    print('x es mayor que y')
elif (x < y):
    print('x es menor que y')
else:
    print('x es igual que y')

"""
Condicionales anidados
"""
x = 4
y = 4
#Evaluar si x > y
if (x > y):
    print('x es mayor que y')
else:
    if (x < y):
        print('x es menor que y')
    else:
        print('x es igual que y')

    
# Evaluar si x es mayor que 0
# Evaluar si x es menor que 10
x = 4
if (x > 0):
    if (x < 10):
        print("x es un número positivo de un dígito")
  
#    True      True
#    True and  True
#        True
if (x > 0 and x < 10):
    print("x es un número positivo de un dígito")