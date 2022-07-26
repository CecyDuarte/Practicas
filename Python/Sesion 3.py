# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:49:47 2020

@author: almac
"""

#%%
#booleanos, verdadero o falso
print(type(True))

a=1
b=2
c="Hola"

print(a>b)

d=bool(c);
print(d)
print(int(d))
print(int(a>b))

#false es 0 y True es 1
#%%
print(type(None))
#Este al ejecutarlo no despliega nada
#dato vacio
#%%

a=2020
b=4040

print(f"¿{a}>{b}?\n", a>b)
print(f"¿{a}<{b}?\n", a<b)
print(f"¿{a}={b}?\n", a==b)
print(f"¿{a} es diferente {b}?\n", a!=b)
print(f"La negación de '{a}!=23' es", not a != 23)

#%%igualmente esta el y & o
print(f"¿{a} != 23 y {a} > {b}?\n", a!=23 and a>b)
print(f"¿{a} != 23 o {a} > {b}?\n", a!=23 or a>b)
#la negacion del or es un nor
#%%
#para comparar un verdaero o falso usas is

Ana=True
print("El valor de Ana es una verdad?\n", Ana is True)
#Y aqui se hace una negacion de lo anterior
print(not(Ana is False))

#%%
#Estructuras basicas de Pyton
#Objetos para almacenar informacion, como arrays, conjuntos
#las matrices son un tipo de estructura

#las listas son las mas importantes, en R no, son un data frame
#Conj de datos que importa el orden, indexado
carreras=["matemáticas", "fisica", "actuaria", "computacion"]

print(carreras)
print(type(carreras))

#lista con varios tipos de elementos
lista1=["Hola", 1+2,1<0]
print(lista1)
print(type(lista1))

#%%indexado de listas o indice
#sintaxis: nombre_lista[inicio:final:orden], mas aqui se le resta 1 al final
print(carreras[0])
print(carreras[0:2])
print(carreras[:2])
print(carreras[1:2])
print(carreras[2:])

#tambien se puede ir hacia atras
print(carreras[-2])

#el orden nos dice la secuencia, es decir, se va brincando de n en n segun le indiquemos
print(carreras[::2])
#el signo negativo en el orden nos dice que va en sentido contrario
print(carreras[::-2])

#%%
#operaciones internas de listas
#para saber cantidad de elementos 
print(len(carreras))
#%%
#en python elementos mutables, es decir, le puedes agregar elementos
#por ejemplo con metodo append
carreras.append("matematicas aplicadas")
print(carreras)
#%%
#tambien podemos concatenar listas
carreras_doble=2*carreras
print(carreras_doble)
#%%
#e incluso concatenar lista diferentes en una
print(carreras+carreras[::-1])
#%%
#tambien se puede cambiar elementos de una lista
carreras[4]="matematicas industriales"
print(carreras)

#%%
#cambiando un rango de elementos o añadir
carreras[2:] = ["Actuaría","Computación", "Matemáticas industriales", "Matemáticas Aplicadas"]
print(carreras)
#%%
#para ver si algo permanece a la lista
print("¿La carrera de biología pertence a la lista de carreras?\n","biología" in carreras)
print("¿La carrera de física pertence a la lista de carreras?\n","Física" in carreras)
print("¿La carrera de física pertence a la lista de carreras?\n","física" in carreras)
#%%
#metodo index es para encontrar el lugar de un elemnto
print(carreras.index("fisica"))

#devuelve indice en que elemento aparece por primera vez
#%%eliminando elementos, dos formas
#metodo pop
#con indice
carreras.pop(4)
print(carreras)
#%%
carreras.pop(carreras.index("fisica"))
print(carreras)

#%%
#metodo para ordenar elementos pero en este modifica al Objeto
carreras.sort()
print(carreras)
#va a buscar un criterio de orden
#como aqui son palabras por orden alfabetico

#%%
#range sirve para generar listas secuenciales
lista2=list(range(15))
print(lista2)
#los elementos van del 0 al 15

#%%
#tupla, son lo mismo que las listas solo que son inmutables
#es decir no podemos modificarla
#y usas () en lugar []



