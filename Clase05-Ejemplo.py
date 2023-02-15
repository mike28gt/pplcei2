#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:34:40 2023

@author: miguelcatalan
"""

# Se solicita el primer operando
numero_1 = input("Ingrese un número entero: ")

mensaje = "Ingrese otro número entero: "

# Se solicita el segundo operando
numero_2 = input(mensaje)

# Se realizar la resta
resta = int(numero_1) - int(numero_2)

# Se muestra el resultado
print("El resultado de la resta es: " + str(resta))