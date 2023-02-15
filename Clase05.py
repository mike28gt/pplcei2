#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:21:16 2023

@author: miguelcatalan
"""

"""
Solicitud de información al usuario (continuación)
    * A la función input() se le puede proporcionar un texto el cual se despliegue como instrucciones para el usuario.
    * Este texto se coloca dentro de los paréntesis y puede ser un str literal o una variable con un dato str.
"""

"""
Conversión de tipos de datos
    * Es cuando convertimos un dato de un tipo en específico a otro tipo.
    * Existen funciones específicas en Python para realizar la conversión de datos
    * int(): convierte un dato str, float o bool a int.
        * Al convertir un str a int, el texto del dato str debe tener el formato de un entero, de lo contrario mostrará un error de tipo ValueError
    * str(): convierte un dato int, float o bool a str 
"""

"""
Comentarios
    * Es texto que el programador coloca dentro de las instrucciones para explicar o hacer notar una funcionalidad a otro programador.
    * Los comentarios NO representan instrucciones para la computadora.
"""

"""
Elección de nombres para las variables 
    * Se deben utilizar siempre nombre representativos de variables

# incorrecto
a = 35.0
b = 12.50
c = a * b
print(c)

# correcto
horas = 35.0
tarifa = 12.50
salario = horas * tarifa
print(salario)

# incorrecto
x1q3z9ahd = 35.0
x1q3z9afd = 12.50
x1q3p9afd = x1q3z9ahd * x1q3z9afd
print(x1q3p9afd)

"""
# correcto
horas = 35.0
tarifa = 12.50
salario = horas * tarifa
print(salario)