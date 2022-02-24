#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
En este módulo deben estar las funciones encargadas de extraer las
estadísticas del archivo de datos, mostrarlas al usuario cuando cuando lo pida, modificarlas al
finalizar la carrera y actualizar el archivo apropiadamente.
'''

def Lectura(Contenido):
    Archivo = open("cod_base_oscar_yepez/hist.log", "r")
    contenido = Archivo.readlines()
    Archivo.close
    return contenido
Lectura("")
    
"""
def Escritura():
    Archivo = open("hist.log")
    Archivo.close
"""
