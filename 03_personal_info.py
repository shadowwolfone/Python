# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:21:11 2019

@author: 1-26-PB-L2-13
"""

while True:
    nombre=input("Ingresa tu Nombre:")
    apellido=input("Ingresa tu Apellido:")
    ubicacion=input("Ingresa tu Ubicación:")
    edad=input("Ingresa tu edad:")
    espacio=" "
    punto="."
    
    if edad =='q' or edad == 'salir':
        print('Gracias')
        break
    
    edad=int(edad)
    if edad <= 25:
        print("Hola"+espacio+nombre+punto+'\n'
          "Tu apellido es"+espacio+apellido+espacio+'\n'
          "Vives en:"+espacio+ubicacion+espacio+'\n'
          "Tu edad es:"+espacio+str(edad)+espacio+punto+'\n'
          "Ere demasiado joven")
    elif edad > 26 and edad <= 35:
        print("Hola"+espacio+nombre+punto+'\n'
          "Tu apellido es"+espacio+apellido+espacio+'\n'
          "Vives en:"+espacio+ubicacion+espacio+'\n'
          "Tu edad es:"+espacio+str(edad)+espacio+punto+'\n'
          "Ere joven")
    else:
        print("Hola"+espacio+nombre+punto+'\n'
          "Tu apellido es"+espacio+apellido+espacio+'\n'
          "Vives en:"+espacio+ubicacion+espacio+'\n'
          "Tu edad es:"+espacio+str(edad)+espacio+punto+'\n'
          "Ya no eres joven")
        