#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:51:36 2023

@author: miguelcatalan
"""

"""
    Ciclo de vida de un objeto
        Constructores: son un tipo especial de método que se ejecuta de forma
                    automática cuando el objeto es creado.
                    Debe tener un nombre en especifico.
        Destructores: son un tipo especial de método que se ejecuta de forma
                    automática cuando el objeto se elimine.
    
    Herencia (Generalización):
        Clase Padre: 
        Clase Hija: 
        
"""


class Animal:
    nombre = ""
    hambre = False
    suenio = False
    
    def __init__(self):
        print("Se ejecuto el constructor")
    
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
            
    def __del__(self):
        print("Se eliminó el objeto")
            








