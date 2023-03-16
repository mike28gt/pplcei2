#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:33:15 2023

@author: miguelcatalan
"""

"""
Estructura repetitiva for
    Es una estructuctura determinada.
    
    for variable_de_iteracion in lista_elementos:
        instrucciones que se van a repetir en la estructura repetitiva
"""

estudiantes = ['Yenifer', 'Elvis', 'Jose']
for estudiante in estudiantes:
    print('Hola:', estudiante)
print('Terminado!')


"""
Bucles de recuento y suma
"""
contador = 0
for valor in [4, 23, 98, 1003, 86, 64]:
    contador = contador + 1
print("La lista tenia ",contador," elementos.");
    

acumulador = 1000
for valor in [4, 23, 98, 1003, 86, 64]:
    acumulador = acumulador + valor
print("Total: ",acumulador)


"""
Bucles de maximo y mínimos
"""
mayor = None
for valor in [4, 23, 98, 1003, 86, 64]:
    if mayor is None or valor > mayor:
        mayor = valor
print('Mayor', mayor)


menor = None
for valor in [4, 23, 98, 1003, 86, 64]:
    if menor is None or valor < menor:
        menor = valor
print('Menor', menor)