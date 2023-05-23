#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 20:13:51 2023

@author: miguelcatalan
"""

"""
Lectura de archivos:
    * Cuando se abre un archivo para escritura, se proporciona el argumento 
      "w" a la función open() lo cual inica que el archivo se desea abrir
      para escritura.
    * Cuando se abre un archivo para escritura y este archivo no existe,
      entonces se va a crear un nuevo archivo con el nombre indicado.
    * Cuando se abre un archivo para escritura y este archivo YA existe,
      entonces el contenido del archivo a ser eliminado (truncado)
    * Los archivos se deben cerrar después de haber sido escritos para
      persistir la información que fue escrita en el archivo.
"""

archivo = open("/Users/miguelcatalan/Desktop/salida.txt", "w"); 

texto = "Esta es otra prueba.\n"
archivo.write(texto)
archivo.write("Esta es otra cadena.")

archivo.close()