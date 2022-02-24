#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
En este módulo deben quedar las funciones que se encargan de interactuar
con el usuario, es decir, de pedirle datos y de mostrarle el juego.
'''
import os
import correr_carrera as carr

def imprimirPista():
    '''
    Esta función no tiene parámetros ni retorna nada. Se encarga consultar la 
    posición en que se encuentra cada carro para dibujar la pista completa
    indicando sus posiciones.
    
    Cada carril tiene un ancho de dos espacios para que quepa el carro 10.
    Y la pista tiene una longitud de 20.
    
    La posición de avance de cada carro se obtiene invocando la función
    posAvance_Pista().
    '''
    cant_carros = 10
    ancho_carriles = len(str(cant_carros))
    long_pista = 20
    
    pista = ( ("|" + " " * ancho_carriles )* cant_carros + "|\n" ) * long_pista
    
    for carro in range(cant_carros):
        pos = int(carr.posAvance_Pista(carro))        
        ubic = 1 + carro * (ancho_carriles + 1) + pos * ((ancho_carriles + 1) * cant_carros + 2)
        pista = pista[:ubic]+ str(carro+1) + " " * (ancho_carriles - len(str(carro+1))) + pista[ubic + len(str(cant_carros)):]  
    print(pista)
    
print(imprimirPista())
