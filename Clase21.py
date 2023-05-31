#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:23:28 2023

@author: miguelcatalan
"""

"""
Listas
    
Métodos de listas
    append()
    extend()
    
Eliminación de elementos
    pop()
    del
    remove()
    Eliminación de más de un elementos

Funciones para listas
    len()
    max()
    min()
    sum()
    
Listas y cadenas
    split()
    join()
    
Listas como argumentos
    Parámetros por referencia
    
"""

# Método append
b = [1, 2, 3, 4]
b.append(5)
b.append(6)
print(b)

# Método extend
b.extend([7, 8, 9])
b2 = [10, 11, 12, 13]
b.extend(b2)
print(b)

# Método sort
b = [9, 12, 4, 5, 100, 23, 54]
print("Lista original:", b)
b.sort()
print("Lista ordenada:", b)

b3 = [4.25, 1.0001, 0.001, 100.1678]
print("Lista original:", b3)
b3.sort()
print("Lista ordenada:", b3)


# Eliminación de elemento de una lista
# pop
c = ['m', 'i', 'g', 'u', 'e', 'l']
print(c)
elemento_eliminado = c.pop(3)
print(elemento_eliminado)
print(c)


print(c)
elemento_eliminado = c.pop()
print(elemento_eliminado)
print(c)

# del
del c[0]
print(c)

c = ['m', 'i', 'g', 'u', 'e', 'l']
del c[2:5]
print(c)

# remove
c = ['m', 'i', 'g', 'u', 'e', 'l']
c.remove("u")
print(c)


#Funciones para listas
b = [9, 12, 4, 5, 100, 23, 54]
# len()
resultado = len(b)
print(resultado)

# max()
resultado = max(b)
print(resultado)

# min()
resultado = min(b)
print(resultado)

# sum()
resultado = sum(b)
print(resultado)

print("Promedio:", sum(b)/len(b))


#Listas y cadenas
cadena = "Python"
l = list(cadena)
print(l)

# split()
linea = "Guatemala felíz que tus aras"
l = linea.split()
print(l)


linea2 = "Miguel,Catalan,Masculino,21"
l = linea2.split(",")
print(l)

#join()
delimitador = "|"
print(delimitador.join(l))






