#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:31:42 2023

@author: miguelcatalan
"""

"""
Funciones definidas por el usuario:
    Para definir una función se utiliza la palabra reservada def
    El nombre no debe empezar con un número y puede estar seguido de números y letras
        El nombre de la función debe ser único
        El nombre de la función no debe coincidir con el nombre de cualquier otra variable
    Seguido del nombre nombre se coloca un par de paréntesis "()"
        Dentro de estos paréntesis se colocan las entradas que necesita la función
        para poder realizar la tarea para la que fue creada
    Después colocamos el símbolo de dos puntos ":"
    Es importante que la función haya sido definida antes de intentar invocarla
"""

def mostrar_coro(): # Encabezado de la función
    # Cuerpo de la función
    print("I can buy myself flowers")
    print("Write my name in the sand")
    

def repetir_coro():
    mostrar_coro()
    mostrar_coro()


repetir_coro()


import math

math.sin(math.pi)
math.pow(2, 3)


def mostrar_doble(nombre):
    print(nombre)
    print(nombre)


mostrar_doble("Miguel")

mostrar_doble("Miguel " * 4)

variable = "Alejandro"
mostrar_doble(variable)

"""
    Funciones productivas: son aquellas que retornan un resultado
    Funciones estériles: son aquellas que NO retornar un resultado
"""

def suma(a, b):
    resultado = a + b
    return resultado


dato = suma(3, 5)
print(dato)


resultado = mostrar_doble("Juan")
print(resultado)