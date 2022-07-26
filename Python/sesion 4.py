# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:07:55 2020

@author: almac
"""

#%%
#objetos tipo dict en la que tienes una coleccion de elementos, pero por clave o como identificacion
#los mas comunes son los string y enteros(int)

#dos maneras de definir diccionario

#sintaxis con llaves
#{<clave 1>:<objeto 1>, ..., <clave n>:<objeto n>}
#orden respetado segun fueron capturados
dict1={"nombre":"Juan", "apellido1":"Perez", "apellido2": "Sanchez"}
print(dict1)
dict2={1.25:"hola",(12,23):"saludo", 12j:True}
print(dict2)
print(type(dict2))


#%%
#funcion dict no es necesario que lleve comillas los nombre de etiquetas
dict(nombre="Armando", escolaridad_maxima="licenciatura")
dict("nombre"="Armando", "escolaridad_maxima"="licenciatura")
dict(1="uno", operador="+")
#%%
#par mapeables
#pares de dos elemetos; objeto inmutable y otro cualquier tipo
#objeto inmutable, aquel que no puedes cambiar sin cambiar la estructura
par_mapeable=(["nombre", "Juan"], ["promedio", 10])
dict4=dict(par_mapeable)
print(type(dict4))
#esto te sirve para cuando quieres convertir una lista a diccionario


#las listas son mutables
#%%
print(dict1["nombre"])
catalogo={"camisas":["algodon", "lino"], "pantalones":["mezclilla"]}
print(catalogo["camisas"][1])

#%%
#modificacion o adccion de un elemento en un objeto tipo dict
#<objeto tipo dict>[<clave>]=<valor>
persona = dict(nombre="Juan", primer_apellido='Perez')
print(persona)
persona['nombre'] = "Joaquín"
print(persona)
persona['segundo_apellido'] = "Sánchez"
print(persona)

#%%
#para aliminar un elemento de un dicicoonario
#sintaxis: del <objeto tipo dict>[<identificador>]
persona = dict(nombre="Juan", primer_apellido='Perez')
del persona['nombre']
print((persona))

#%%
#metodo del tipo dict

#metodo copy: copian un diccionario
persona = {"nombre": "Juan", "primer_apellido":"Pérez", "segundo_apellido":"Sánchez"}
id(persona)
#la funcion id me va a decir donde esta guardado
#si tengo el mismo numero es que son el mismo
otra_persona = persona.copy()
id(otra_persona)
print(otra_persona)
print(persona == otra_persona)
print(persona is otra_persona)
#me quede en el 39:42

#%%
#metodo pop
persona = {"nombre": "Juan", "primer_apellido":"Pérez", 
           "segundo_apellido":"Sánchez"}
persona.pop("nombre")
print(persona)
#elimina el elemento del que le das una clave
persona.pop("nombre")
print(persona)
#en caso de no tenerlo, te marca error
#solo puedes ir eliminando de uno en uno, en caso contrario, puedes utilizar un while

#%%
#metodo popitem
persona = {"nombre": "Juan", "primer_apellido":"Pérez", "segundo_apellido":"Sánchez"}
persona.popitem()
print(persona)
persona.popitem()
print(persona)
persona.popitem()
print(persona)
persona.popitem()
#se supone que quita de forma aleatoria los elementos y los restantes los convirte en tupla
#pero solo en versiones anteriores a 3.7
#en esta elimina el ultimo argumento
#%%
#metodo get
#se utiliza para regresar valores 
persona = {"nombre": "Juan", "primer_apellido":"Pérez", "segundo_apellido":"Sánchez"}
persona.get("nombre")
persona.get("nombre1")
persona["nombre1"]
print(persona.get("nombre1"))
persona.get("nombre1", False)

#%%
#metodo update: sustituye y añade elementos que se ingresan como argumentos
persona = {"nombre": "Juan", "primer_apellido":"Pérez", "segundo_apellido":"Sánchez"}
persona.update({"nombre":"Pedro", "codigo_postal":"020101"})
print(persona)
persona.update({'nombre':'Pedro'})
print(persona)
persona.update([("profesion", "abogado"), ["nacionalidad", "MX"]])
print(persona)

#%%
#metodo setdefault()
#muy parecido al update
persona = {"nombre": "Juan", "primer_apellido":"Pérez", "segundo_apellido":"Sánchez"}
persona.setdefault("email", "jp@falso.com")
print(persona)
persona.setdefault("nombre", 'José')
print(persona)
#en caso de no ponerle nada, te aparece None
persona.setdefault("membresia")
print(persona)
#me quede 1:09:44

#%%
#metodo fromkeys()
#le estoy dando de comer un objeto iterable, es decir, puedo pasar elemento por elemento
dict.fromkeys(["nombre", "apellido"])
#esta creando un diccionario a partir del nombre de las claves
persona = dict.fromkeys(["nombre", "apellido"], True)
print(persona)
dict.fromkeys(["nombre", "apellido"], "Pendiente")
print(persona)

#%%
#metodo clear: elimina todos los elementos de un diccionario
persona = {"nombre": "Juan", "primer_apellido":"Pérez", "segundo_apellido":"Sánchez"}
print(persona)
persona.clear()
print(persona)

#%%
#metodos que generan objetos iteradores
#metodo keys
#iterar: puedes brincar de elemento en elemento
#nos imprime las claves
persona = {"nombre": "Juan", "primer_apellido":"Pérez", "segundo_apellido":"Sánchez"}
claves = persona.keys()
print(claves)
print(type(claves))

for clave in claves:
    print(clave)
print(tuple(claves))
#%%
#metodo values
#nos devuelve valores

persona = {"nombre": "Juan", "primer_apellido":"Pérez", "segundo_apellido":"Sánchez"}
valores = persona.values()
print(type(valores))
print(valores)
for valor in valores:
    print(valor)
print(set(valores))
