#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 20:33:24 2023

@author: miguelcatalan
"""

"""
    Operador in
        No tiene la misma funcionalidad que tiene el operador in en la sentencia for
        Evalua si una cadena es subcadena de otra. Si la cadena es una subcadena entonces retorna True de lo contrario retorna False
"""

resultado = "Miguel" in "Miguel Catalan"
print(resultado)

resultado = "David" in "Miguel Catalan"
print(resultado)

resultado = "a" in "Miguel Catalan"
print(resultado)

resultado = "I" in "Miguel Catalan"
print(resultado)


"""
    Comparación entre cadenas
        Operador para comparar cadenas es: ==
        Cuando se utilizan los operadores > y < se compara la posición en la que se encuentran las letras dentro del abecedario.
        Python coloca las letras mayúsculas antes que las minúsculas
"""

resultado = "Miguel " == "Miguel "
print(resultado)

resultado = "MigueL" == "Miguel"
print(resultado)

nombre = "Miguel"
resultado = nombre == "Miguel"
print(resultado)

resultado = "asno" < "casa"
print(resultado)

resultado = "asno" < "Casa"
print(resultado)


"""
    Métodos de cadenas
        Dentro de Python todas las variables son objetos
        Los objetos se crean a partir de clases 
        Las clases se encuentran divididas en:
            1.- atributos: características de un objeto
            2.- métodos: acciones que se pueden realizar con el objeto
        En los objetos el operador punto proporciona el acceso a los atributos y métodos de un objeto
"""

palabra = "naranja"
nueva_palabra = palabra.upper()
print(nueva_palabra)

indice = palabra.find("an")
print(indice)

# El valor de -1 indica que no se encontró la subcadena
indice = palabra.find("an", 4)
print(indice)

linea = "   Hola    "
nueva_linea = linea.strip()
print(linea)
print(nueva_linea)

linea = "   Hola    mundo    "
nueva_linea = linea.strip()
print(linea)
print(nueva_linea)

linea = "Excelente día!"
resultado = linea.startswith("Excelente")
print(resultado)

linea = "Excelente día!"
resultado = linea.startswith("día")
print(resultado)


"""
    Análisis de cadenas
"""

#Extraer el dominio del correo electrónico
texto = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

indice_arroba = texto.find("@")
print(indice_arroba)

indice_blank = texto.find(" ", indice_arroba)
print(indice_blank)

dominio = texto[indice_arroba+1:indice_blank]
print(dominio)






