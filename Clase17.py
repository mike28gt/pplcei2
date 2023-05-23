#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:58:08 2023

@author: miguelcatalan
"""

"""
Programación Estructurada
    Por medio de tres tipos de estructras se puede 
    construir cualquier programa.
        1.- Secuenciales
        2.- Selectivas
        3.- Repetitivas

Programación Orientada a Objetos
    Reutilizar de forma más eficiente el código.

    Abstracción: seleccionar los características y comportamientos
    que sean relevantes de un objeto de la vida real.

    Clase: definen la estrutura de los objetos.
        Entendemos como estrutura las características y comportamientos 
        de un objeto de la vida real.
        
        Abstracción de un teléfono celular:
            Características (cosas que describen al objeto):
                - Marca
                - Tamano de la pantalla
                - Capacidad de almacenamiento
                - Color
                - Modelo
                - Resolución de la camara
            Comportamientos (las cosas que puede hacer el objeto):
                - Llamar
                - Tomar fotografía
                - Enviar mensajes de texto
                - Reproducir música
                - Navegar en Internet
                - Compartir documentos
                
        Las clases están compuestas de abstracciones de objetos, lo cual
        implica que una clase contiene características y comportamientos
        de un objeto de la vida real.

    Objeto:
        Los objetos son instancias de la clases. 
        
        Utilizando la clase Teléfono Celular:
            
            Objeto 1:
                - Marca: IPhone
                - Tamano de la pantalla: 7"
                - Capacidad de almacenamiento: 128GB
                - Color: Negro
                - Modelo: 14
                - Resolución de la camara: 25Mp
                
            Objeto 2:
                - Marca: Samsung
                - Tamano de la pantalla: 9"
                - Capacidad de almacenamiento: 256GB
                - Color: Blanco
                - Modelo: S22
                - Resolución de la camara: 50Mp
                
            Objeto 3: ...
    
    Características
    
    Comportamientos

    Atributos:
        Son las caracteristicas de las clases y son representadas
        programaticamente por medio de variables.
    
    Métodos:
        Es el equivalente a una función dentro del a Programación
        Orientada a Objetos.
        Todos los métodos reciben por defecto un parámetro de nombre
        self
    
    
    La palabra reservada class le indica a Python que se está definiendo
    una nueva clase.
    Idealmente cada clase se debe almacenar en un archivo propio.
    Existe una convención respecto a que los nombres de las clases deben iniciar
    con letra mayúscula.
"""

class TelefonoCelular:
    
    #Características / Atributos
    marca = ""
    tamano_pantalla = 0
    capacidad_almacenamiento = 0
    color = ""
    modelo = ""
    resolucion_camara = 0
    
    #Comportamientos / Métodos
    def llamar(self):
        print("Llamando...")
        
    def tomar_fotografia(self):
        print("Tomando fotografía...")
        
    def enviar_mensaje_de_texto(self):
        print("Enviando mensaje de texto...")
        
    def reproducir_musica(self):
        print("Reproduciendo música...")
        
    def navegar_internet(self):
        print("Navegando en Internet...")
        
    def compartir_documentos(self):
        print ("Compartiendo documento...")
        
# Creación de objetos

objeto1 = TelefonoCelular()
objeto1.marca = "iPhone"
print(objeto1.marca)
objeto1.llamar()

objeto2 = TelefonoCelular()
objeto2.marca = "Samsung"
print(objeto2.marca)
objeto2.navegar_internet()

objeto3 = TelefonoCelular()
objeto3.marca = "Huawei"
print(objeto3.marca)
objeto3.tomar_fotografia()

"""
    Crear una clase persona definiendo sus atributos y métodos
    Crear un objeto de tipo persona y asignarle valores a sus
    atributos.
"""


"""
    
    Creación de la clase Animal
    
    Creación de un nuevos objetos
    
    Operador punto
    
    Ciclo de vida de un objeto
    
    Herencia
"""