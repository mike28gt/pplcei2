#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:25:59 2023

@author: miguelcatalan
"""

"""
    Los datos de tipo cadena son datos compuestos. 
    Las cadenas estan compuestas de caracteres (caracter: es cualquier símbolo que se pueda representar en la computadora)
    Dentro de una cadena cada caracter se encuentra en una posición en específico. A esta posición se le llama índice.
    Python inicia el enumeración de índices desde el 0 (NO inicia en el 1)
        Los índices solamente pueden ser números enteros
        El índice debe existir dentro de la cadena
"""

fruta = "naranja"

#cadena: naranja
#índice: 0123456

print(fruta[4])

"""
    Para saber cuantos caracteres tiene una cadena utilizamos la función len
    Si se desea acceder al último elemento (caracter) de una cadena de la cual no se conoce su longitud se puede utilizar la expresión cadena[len(cadena) - 1]
        Lo anterior debido a que la enumeración de los índices empieza en 0 y no en 1
"""

cantidad_de_caracteres = len(fruta)
print(cantidad_de_caracteres)

# Ejemplo: mostrar el último caracter de la cadena ingresada por el usuario
ejemplo_cadena = input("Ingrese una cadena: ") #carro
indice = len(ejemplo_cadena) #5
ultimo_caracter = ejemplo_cadena[indice - 1] #ejemplo_cadena[4]
print(ultimo_caracter)


"""
    Se puede acceder a los caracteres de una cadena utilizando índices negatios
    Cuando se utilizan índices negativos la numeración de indices empieza en -1 y este índice se le asigna al último caracter de la cadena
"""

# cadena: n a r a n j a    -- Ignorar los espacios en blanco
#        -7-6-5-4-3-2-1

print(fruta[-2])

"""
    Recorrido de cadenas:
        Se utilizan bucles e índices
"""

indice = 0
while indice < len(fruta):
    print(fruta[indice])
    indice = indice + 1
    

for caracter in fruta:
    print(caracter)


"""
    Rebanado de cadenas
        Es la obtención de secciones de una cadena, que se encuentren constuituidos por caracteres consecutivos dentro la cadena
        Para esto se utiliza la notación cadena[limite_inferior:limite_superior].
            El índice representado por limite_inferior se incluye dentro de la subcadena
            El índice representado por limite_superior NO se incluye en la subcadena
            Si se omite el limite inferior Python asigna por defecto el índice 0
            Si se omite el limite superior Python asigna por defecto el último índice de la cadena
        Una cadena vacía es aquella que no contiene ningún caracter.
"""

# cadena: naranja
# índice: 0123456

subcadena = fruta[2:5]
print(subcadena)

subcadena = fruta[:5]
print(subcadena)

subcadena = fruta[2:]
print(subcadena)

subcadena = fruta[3:3]
print(subcadena)


"""
    Las cadenas son inmutables. Significa que las cadenas no pueden ser modificadas.
"""

saludo = "Hola mundo!"
#saludo[0] = "h"
#print(saludo)

nuevo_saludo = "h" + saludo[1:]
print(nuevo_saludo)

"""
    Conteo de caracteres repetidos
"""

#palabra = "Miguel Catalan"
palabra = input("Ingrese una palabra: ")
contador = 0
for caracter in palabra:
    if caracter == "a":
        contador = contador + 1

print(contador)
