#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:05:51 2023

@author: miguelcatalan
"""

"""
Estructuras repetitivas
    Se encarga de ejecutar un bloque de código un determinado 
    número de veces
"""

"""
Contadores
    Cuando se actualiza una variable en una unidad en base
    al valor que tenía asignado previamente
"""
x = 0
print("Linea 21: ", x)
# Contador incremental
# Primero se resuelve el lado derecho del símbolo de 
# asignación
x = x + 1
print("Linea 26: ", x)
x = x + 1
print("Linea 28: ", x)
x = x + 1
print("Linea 30: ", x)

# Contador decremental
x = x - 1
print("Linea 34: ", x)
x = x - 1
print("Linea 36: ", x)
x = x - 1
print("Linea 38: ", x)
x = x - 1
print("Linea 40: ", x)
x = x - 1
print("Linea 42: ", x)

"""
Estructura repetitiva while

while expresion_logica/expresion_comparativa:
    listado de instrucciones que deseamos se ejecuten
    
    Flujo de ejecución de la estructura repetitiva while
    1: Se evalua la condición (puede dar como resultado True o False)
    2: Si la condición es False, se sale de la sentencia while y se continúa la ejecución de la siguiente sentencia al while
    3: Si la condición es True, se ejecuta el cuerpo del while y luego se regresa al paso 1.
"""
i = 0
while i <= 5:
    print(i)
    i = i + 1
print("Se finalizó el conteo.")

j = 0
while j >= -10:
    print(j)
    j = j - 1
print("Se finalizó el conteo.")

"""
Estructura repetitiva infinta:
    Se repiten de forma indeterminada (de forma infinita)
"""

#n = 0
#while (True):
#    print(n, end=' ')
#    n = n - 1
#print('Termina la estructura repetitiva')

"""
Instrucción break
    Finaliza la ejecución de una estructura repetitiva 
    de forma instantanea
"""
while (True):
    texto = input("Ingrese una palabra: ")
    if (texto == "fin"):
        break
    print(texto)
print("Termina la estructura repetitiva")

"""
Instrucción continue
    Omitir las instrucciones que se encuentre a continuación
    de la instrucción y regresar de forma inmediata a evaluar
    la expresión de la estructura repetitiva
"""
while (True):
    texto = input("Ingrese una palabra: ")
    if (texto[0] == "#"):
        continue
    if (texto == "fin"):
        break
    print(texto)
print("Termina la estructura repetitiva")

