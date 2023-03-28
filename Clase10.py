#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:25:38 2023

@author: miguelcatalan
"""



"""
Funciones:
    * Son conjuntos de instrucciones.
    * Tiene un nombre único. El nombre de una función debe cumplir 
      con las mismas reglas que el nombrando de una variable
    * Las funciones pueden recibir datos de entrada (argumentos)
    * Las funciones pueden retornar datos (valor de retorno)
    
Funciones internas: son todas aquellas que provee Python
Funciones definidas por el usuario: son funciones que define el usuario

Ejemplos de funciones internas:
"""

print(type(32))

print(max('Hola mundo'))

print(min('Hola mundo'))

print(len('Hola mundo'))

print(int('32'))

print(float(32))

print(str(32.23))

"""
Módulos:
        * son conjuntos de funciones.
        * para poder utilizar un módulo este debe ser importado
        * para importar módulo se utiliza la palabra reservada import
        * para utilizar las funciones dentro de un módulo se debe utilizar
          el operador punto (.)
        * los módulos además de funciones tambien puede proveer
          constantes
"""

import math

print(math.log10(32))

radianes = 0.7
res = math.sin(radianes)
print(res)

raiz_cuadrada = math.sqrt(4)
print(raiz_cuadrada)

print(math.pi)

r = 2.0
area_circulo = math.cos(math.pi) * math.pow(r, 2)
print(area_circulo)


"""
Módulo random
    Provee funciones para la manipulación de números aleatorios.
    Entendemos como número aleatorio números al azar.
    
    * función random(): retorna un número aleatorio entre 0.0 y 1.0 (incluye
      al 0.0 pero excluye al 1.0)
"""

import random

print(random.random())

print(random.randint(5, 10))

lista = [1, 99, 73, 25]
print(random.choice(lista))
    

