#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:16:40 2023

@author: miguelcatalan
"""

"""
Ejercicio:
    
1 - Elabore una abstracción del objeto animal:
    1.1 - Debe incluir las características:
        1.1.1 - Nombre
        1.1.2 - Hambre
        1.1.3 - Suenio
        1.1.4 - Agregue otras 2 características
    1.2 - y los comportamientos:
        1.2.1 - Desplazarse
        1.2.2 - Comer
        1.2.3 - Dormir
        1.2.4 - Agregue otros 2 comportamientos
2 - Transforme la abstracción anterior en una clase Animal.
3 - Construya 3 objetos de tipo Animal y asigne valores a cada una de
sus propiedades e invoque a cada uno de sus métodos.
"""


class Animal:
    nombre = ""
    hambre = False
    suenio = False
    
    def desplazarse(self):
        print("Me estoy desplazando...")
        
    def comer(self):
        if (self.hambre == True):
            print("Estoy comiendo...")
        else:
            print("No tengo hambre...")
        
    def dormir(self):
        if (self.suenio == True):
            print("Estoy durmiendo... zzz...")
        else:
            print("No tengo suenio...")
        
        
animal_1 = Animal()
animal_1.nombre = "Elefante"
animal_1.comer()

animal_1.hambre = True
animal_1.comer()


animal_1.dormir()
animal_1.suenio = True
animal_1.dormir()