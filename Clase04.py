#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:41:53 2023

@author: miguelcatalan
"""

"""
Operaciones con cadenas
    * concatenación: es la unión de dos o más cadenas
    * Su operador es el símbolo +
"""
var_1 = 3 + 4
print(var_1)

var_2 = 3.0 + 2.55
print(var_2)

var_3 = "Hola " + "mundo" + "!" 
print(var_3)
print(type(var_3))

nombre = "Miguel"
saludo = "Hola " + nombre
print(saludo)

print ("Mucho gusto " + nombre)
print (nombre + " Mucho gusto")

"""
Solicitud de información al usuario
    * La captura de datos del usuario desde la pantalla se realiza con la instrucción input()
    * La función input() pausa la ejecución del programa en espera que el usuario ingrese un dato y presione la tecla Enter
    * Los datos capturados por input() representan datos str
"""
dato_del_usuario = input()
print("Este es el dato ingresado por el usuario: " + dato_del_usuario)
print(type(dato_del_usuario))