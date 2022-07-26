# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Esto es un comentario
#%%
print("Hola mundo")
#%%
Resultado=2+2

print(Resultado)

#celda de spyder te ayuda a separar codigo para que no se ejecute todo
#%%
print("hola amor")

#%%
sumari=2+4
print(sumari)
#%%
#este es un metodo, llamado format, que permite insertar strings dentro de otro string
#es decir insertar frases dentro de otras frases
curso1="CDD_Py"
instructor1="Hector"
presentacion="Hola; bienvenidos al Diplomado {} de SciData. \nTu instructor es {}".format(curso1,instructor1)
print(presentacion+"\n")

#%%
#en lugar de format se puede utilizar f-string y aplicar directamente
print(f"hola. Soy {instructor1} de Scidata. Bienvenido al curso {curso1}.")

#%%
#Otros metodos importantes de los strings de Python son upper, lower y capitaliza
nombre_curso="ciencia de datos con Python"
print(nombre_curso.upper())
print(nombre_curso.lower())
print(nombre_curso.capitalize())
#upper=letra mayusculas, lower=letra minusculas, capitalize=tipo oracion
#estos no modifican el texto
#%%
#Hay metodos para eliminar, reemplazar o particionar caracteres
Nombre_puntos="Manuel..."
print(Nombre_puntos.strip("."))
#quita puntos
print(Nombre_puntos.replace("nuel", "riano"))
#reemplaza
print(Nombre_puntos.strip(".").replace("nuel", "riano"))
#elimina y reemplaza

Nombre_Completo="Hector_Manuel_Garduño"
print(Nombre_Completo.split("_"))
#particiona caracteres en una lista
#para mandar a llamar indices en una lista, la variable debe de ser de tipo entero

#%%
#convertir string a numero y ya puedo realizar operaciones
num_str="2020.4"
print(float(num_str)/2)
#en este caso usamos flotante porque debido al punto no puedo convertirlo en entero
#solo podemos hacer esto si quitamos los decimales
print(int(float(num_str)/2))
#me quede en 1:55:12

#%%
#estas son las operaciones basicas que se pueden utilizar
print("la suma, la resta, el producto y la division de 2 y 3 es", 2+3,",",2-3, ", ", 2*3, "y", 2/3, "respectivamente")
#operaciones más complicadas siguen esta sintaxis
a=5;b=3
print(a//b)
#division entera
print(a%b)
#residuo
print(a**b)
#potencia








