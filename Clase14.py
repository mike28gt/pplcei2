#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 20:17:17 2023

@author: miguelcatalan
"""

import sys

"""
Archivos:
    Archivos de texto: Son aquellos que almacenan texto.
    Apertura de archivos en Python:
        
"""

archivo = open("/Users/miguelcatalan/Desktop/ejemplo.txt")
print(archivo)

#archivo = open("/Users/miguelcatalan/Desktop/ejemplo_error.txt")
#print(archivo)

"""
    Archivos de texto y lineas
"""

print("Esto se esta escribiendo en una sola línea")

print("Esto se \n esta escribiendo \n en dos líneas")


"""
Lectura de archivos
"""

# Opción 1: Cuando el archivo es muy grande. Lectura de archivos línea por línea

archivo = open("/Users/miguelcatalan/Desktop/ejemplo.txt")
contador = 0

for linea in archivo:
    contador = contador + 1
    
print("Contador de líneas:", contador)

# Opción 2: Cuando el archivo no es muy grande. Lectura del contenido del archivo en su totalidad

archivo = open("/Users/miguelcatalan/Desktop/ejemplo.txt")

texto = archivo.read()
print(len(texto))


"""
Búsqueda en archivos
"""
archivo = open("/Users/miguelcatalan/Desktop/ejemplo.txt")

for linea in archivo:
    linea = linea.rstrip()
    if linea.startswith("Y "):
        print(linea)
        
        
"""
Permitir a los usuarios elegir el nombre del archivo a operar.
"""

nombre_archivo = input("Cuál es el nombre del archivo a operar: ")

archivo = open(nombre_archivo)

for linea in archivo:
    linea = linea.rstrip()
    if linea.startswith("Y "):
        print(linea)

"""
try, except, open
"""

nombre_archivo = input("Cuál es el nombre del archivo a operar: ")


try:
    archivo = open(nombre_archivo)
except:
    print("No se puede abrir el archivo.")
    sys.exit()

for linea in archivo:
    linea = linea.rstrip()
    if linea.startswith("Y "):
        print(linea)





