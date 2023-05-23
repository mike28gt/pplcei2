#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:27:46 2023

@author: miguelcatalan
"""

"""
Escribe un programa que lea un archivo e imprima su contenido (línea por línea), 
todo en mayúsculas.
"""

#mbox_short_file = open("mbox-short.txt")

#for linea in mbox_short_file:
#    print(linea.upper().rstrip())

"""
Escribe un programa que solicite a un usuario un nombre de archivo y después 
lea ese archivo buscando las líneas que tengan la siguiente forma:

X-DSPAM-Confidence: 0.8475

** Cuando encuentres una línea que comience con “X-DSPAM-Confidence” ponla 
aparte para extraer el número decimal de la línea. Cuenta esas líneas y después 
calcula el total acumulado de los valores “spam-confidence”. Cuando llegues al 
final del archivo, imprime el valor medio de “spam-confidence”.
"""

nombre_archivo = input("Ingrese nombre del archivo a operar: ")

file = open(nombre_archivo)

cantidad_lineas = 0
acumulador_spam_confidence = 0

for linea in file:
    if (linea.startswith("X-DSPAM-Confidence") == True):
        
        indice_espacio_blanco = linea.find(" ")
        cadena_decimal = linea[indice_espacio_blanco + 1:]
        acumulador_spam_confidence = acumulador_spam_confidence + float(cadena_decimal)
        
        cantidad_lineas = cantidad_lineas + 1
        
        print(cantidad_lineas, linea.rstrip())
        
print("cantidad de lineas:", cantidad_lineas, 
      "sumatoria spam confidence:", 
      acumulador_spam_confidence)

promedio_dspam_confidence = acumulador_spam_confidence / cantidad_lineas

print("El valor medio de spam-confidence es de:", promedio_dspam_confidence)



