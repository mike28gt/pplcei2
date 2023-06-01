#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:39:10 2023

@author: miguelcatalan
"""

"""
Diccionarios
    Clave
    Valor
    dict
    Crear diccionario vacío
    Agregar elementos a un diccionario
    Acceder a un elemeto de un diccionario
    Función len()
    Operador in
    Método values()
    Diccionarios como "histogramas"
    Recorrer un diccionario con bucles
"""

# Analogía con estudiantes
# Clave          Valor
# 5312-22-00001  Miguel Catalán
# 5312-21-99999  Juan Perez
# ...
# ...

# Crear diccionario vacío
var1 = dict()
#print(var1)


# Agregar datos a un diccionario
var1['5312-22-00001'] = 'Miguel Catalan'
#print(var1)

var1['P001AAA'] = 'Honda'
print(var1)


# Acceder a un elemento de un diccionario
print(var1['5312-22-00001'])
print(var1['P001AAA'])


# Función len
longitud = len(var1)
print(longitud)


# Operador in
resultado = 'Miguel' in var1
print(resultado)

resultado = 'P001AAA' in var1
print(resultado)


# Método values()
listado_de_valores = var1.values()
print(listado_de_valores)

resultado = 'Miguel Catalan' in listado_de_valores
print(resultado)


# Método keys()
listado_de_llaves = var1.keys()
print(listado_de_llaves)


# Diccionarios como histogramas
palabra = "murcielago"

# m = 1
#u = 1
#r = 1
#c = 1
#i = 1
#e = 1
#l = 1
#a = 1
#g = 1
#o = 1

palabra = "mesopotamia"

# Clave   Valor (la frecuencia de aparición de una letra)
# m     = 2
# e     = 1
# s     = 1
# o     = 2
# p     = 1
# t     = 1
# a     = 2
# i     = 1


histograma = dict()
for letra in palabra:
    print(letra)
    
    if (letra in histograma):
        histograma[letra] = histograma[letra] + 1
    else:
        histograma[letra] = 1

print(histograma)


# Recorrido de un diccionario utilizando bucles
for clave in var1:
    print(clave)
    print(var1[clave])






























