#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Es el programa principal donde debe estar la estructura general del juego y desde
donde se deben invocar las principales funciones de los otros módulos para el desarrollo del
juego.
'''
#librerias_externas
import os

#librerias_locales
#import correr_carrera
import historial_carros
#import interfaz_usuario

#Definimos variables de información.
info_description_game = "---> Este programa simula un juego de carreras, en cual te permitira apostar por un carro, cabe resaltar que son 10 competidores. \n"
info_option_selection = "---> Para iniciar seleciona una de las siguientes opciones \n"

#Variables que dan el funcionamiento de While, para seleccionar una opción.
info_instructivo = "Debes selecionar una de las tres opciones, marca en tu teclado cualquiera de las siguiente teclas, "
opciones = ("1. Carrera", "2. Ver historial", "3. Salir")
opciones_print = ["Carrera", "Ver historial", "Salir"]
D_Permitidos = ["1", "2", "3"]
cdnal_eva = True  # Condicional evaluativo, para el While, y para el if que determina que opción seleciono el usuario. 
user_solicitud = 0
rst_ps = 0
valor_opcion = None


# Recibe el valor de esta variable, ejecutando el programa.
def Iniciar_Jugar(cdnal_eva):
    """Descripcion de la función...
    Esta función le pide al usuario que seleccione una opción y despues evalua retornando este valor para evaluarlo en el ambito de Iniciar.
    """
    #Definimos la variables globales a utilizar en este ambito.
    global info_description_game, info_option_selection, opciones, ciclo, rst_ps
    #Iniciamos la ejecución del programa, pidiendole al usuario que elija una opción.
    while cdnal_eva == True:
       #Verificamos que el usuario halla ingresado uno dato correcto.
        if ciclo == 0:
           user_solicitud = (input("Elija una opción, "))
           ciclo += 1
           
        elif ciclo < 1:
           user_solicitud = (input("Te has equivocado, ingresa otra vez, otra opción, "))
           ciclo += 1
           
        elif ciclo > 1:
           user_solicitud = (input("Otra vez te has equivocado, ingresa otra vez, otra opción, trata de que esta vez sea correcta, "))
           ciclo += 1

        elif ciclo >= 4:
           print(info_instructivo, D_Permitidos)
           ciclo = 0  # Reiniciamos el ciclo
           os.system("clear")# Utilizamos esta linea de codigo para limpiar la pantalla.

        if user_solicitud in D_Permitidos:
            # Le restamos 1 para acceder a la posición que se determina en python.
            user_solicitud = int(user_solicitud) - 1

            if user_solicitud <= len(opciones):
                # Resultado de posición
                rst_ps = opciones_print[user_solicitud]
                cdnal_eva = False
                os.system("clear")
                print("Haz seleccionado,", rst_ps, end="\n")

def Iniciar(cdnal_eva):  # De acuerdo al resultado de la función
    """
    Esta funcion contiene toda la estructura principal del programa, 
    """
    #Definimos las variables globales a utilizar
    global info_description_game, info_option_selection, opciones, ciclo
    
    #Imprimos la información inicial del programa del programa.
    print(info_description_game + info_option_selection, opciones [:])
    
    #Iniciamos la ejecución 
    Iniciar_Jugar(cdnal_eva)
    
    #Determinartamos la opcion que tomo el usuario y la asignamos a la variable de entrada de la función Iniciar.
    while cdnal_eva == True:
        if rst_ps in opciones:
            # Estamos determinando la posición que ha selecionado el usuario para añadirla, a la variable user_solicitud.
            print("Selecionaste,", rst_ps)
            cdnal_eva = False
            valor_opcion = opciones[user_solicitud]
        else:
            break

    #Comprobamos que función se utilizara ahora, para proceder con la siguiente ejecución.     
    if valor_opcion == opciones[0]:
        def Opcion_Carrera():
            #interfaz_usuario.imprimirPista()
            #print(interfaz_usuario.imprimirPista)
            print("Funciona el retorno de Opción carrera")

    elif valor_opcion == opciones[1]:
        def Opcion_Ver_historial():
            historial_carros.Lectura("")
            
    elif valor_opcion == opciones[2]:
        def Opcion_Salir():
            #os.system("clear")
            print("Funciona el retorno de Opción salir")
    else:
        return ("Error en la función iniciar")

print(Iniciar(cdnal_eva))
