#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:41:51 2023

@author: miguelcatalan
"""

"""
Listas
    ¿Cómo se definen las listas?
    Listas anidadas
    Índices
    Listas vacías

Mutabilidad de listas
    Mutabilidad en listas
    Operador in

Recorrido de una lista
    Recorrido para obtener los elementos de una lista
    Recorrido para escribir o actualizar elementos de una lista
    
Operaciones de listas
    Concatenación de listas (operador +)
    Repetición de listas (operado *)
    
Rebanado de listas

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

# Datos primitivos
a = 1
respuesta = True

# Definición de listas
b = [1, 2, 3, 4]
c = ['Hola mundo' , 'Adios', 'Nos vemos después']
# Las listas pueden contener datos de diferente tipo
d = ['Hola mundo', 4, True, ['Otra', 'lista']]

# Listas anidadas
lista_anidadas = [[1, 2], [['a', 'b'], [[True, False], [1.23, 1.34]]]]

# Índices
print(lista_anidadas[0][1])

#print("Valores de la lista:", b)
#indice = int(input("Ingrese el indice del elemento al que desea acceder: "))
#print("El dato que se encuentra en el índice", indice, "es", b[indice])

# Listas vacías
lista_vacia = []

# Mutabilidad de las listas
# b = [1, 2, 4, 4]
b[2] = 4
print(b)

nombres = ['ANTHONY', 'BEXEL', 'BRAYAN']
resultado = 'ANTHONY' in nombres
print(resultado)

# Recorrido para obtener los elementos de una lista
for nombre in nombres:
    print(nombre)
    
# Recorrido para modificar o asignarle 
print(len(nombres))
print(range(10))

for i in range(len(nombres)):
    print (nombres[i])
    
# Concatenación de listas (+)
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
print(lista_1 + lista_2)

# Repetición de listas
lista_3 = nombres * 2
print(lista_3)


#Rebanado de lista
#b = [1, 2, 3, 4]
resultado = b[1:4]
print(resultado)


