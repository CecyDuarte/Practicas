# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:56:06 2020

@author: almac
"""

#crear fecha y horas actuales
import datetime 

ahora=datetime.datetime.now()
print("Fecha y hora actuales: ", ahora)

#%%
#la fecha y hora pueden configurar su formato
print(type(ahora))

ahora_formato=ahora.strftime("%H:%M:%S %Y-%m-%d")
print(ahora_formato)

#%%
#Solicitar al usuario el radio de un circulo y calcular su area
pi=3.1416
radio=float(input("Introduce el radio del circulo "))

area=(radio**2)*pi
print(f"el area de la circunferencia es {area} con radio {radio}")

#%%
#Solicitar nombre a usuario y obtener su representación en orden inversso

nombre=input("Por favor introduce tu nombre: ")
if nombre.isalpha()=="True"or " " in nombre:
    print(f"Su nombre es: {nombre}")
    nombre_invertido=nombre[::-1]
    print(f"Su nombre invertido es: {nombre_invertido}")
else:
    print("Introduce solo letras")
