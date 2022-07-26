# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:54:22 2020

@author: almac
"""

#%%
#iteraciones con ciclos
#for
#iteradores:str.list.tuple.dict.set.frozenset.bytes.
# estructura For: for <nombre> in <iterable>:
for letra in "CHAPULTEPEC":
     print(letra)   
for item in ["uno", "dos", 3]:
    print(item)
#%%
#for con fn range(inicio, final, incrementos)
for contador in range(8):
    print(contador)
#cuenta del 0 al 7 con incrementos de 1
for contador in range(5, 9):
    print(contador)
#cuenta del 5 al 9 con incrementos de uno
for contador in range(3, 11, 2):
    print(contador)
#cuenta del 3 al 11 con incrementos de 2
for contador in range(26, 10, -4):
    print(contador)
#cuenta del 26 al 10 con incrementos de -4
#aqui aunque le pongamos hasta cierto numero aplica un rebanado, por lo que llega hasta un numero antes
for elemento in [1,2,[1,2,3],5,[1,3412,454]]:
    print(elemento)
max([1,2,3])
#%%
#desempaquetado
#La declaración for ... in es capaz de realizar el desempaquetado de colecciones contenidas dentro de un objeto iterable cuando se definen más de un nombre. La condición es que el tamaño de las colecciones que regrese el objeto iterable sea igual al numero de nombres definidos después del for.

palabras = ["gato", "pato", "zeta", "cita"]
#con este for desempacará en primera, segunda, tercera, cuarta item 
for item in  palabras:
    print(item)
for primera, segunda, tercera, cuarta in palabras:
    print(primera)
    print(segunda)
    print(tercera)
    print(cuarta)
    print("----------")
#desempaca aqui las palabras de 4 letras en 4, por 
#%%
#funciones: son piezas de codigo que son delimitadas y llamadas por su nombre
#funcion minima
def funcion():
    pass
#el pass evita que se genere un error de identificacion
funcion()
print(funcion())
type(funcion)
#%%
#funcion con codigo
def saludo():
    print('Hola')
saludo()
def saludo():
    '''Imprime un mensaje de texto'''
    print('Hola')
help(saludo)
#help documenta la funcion 
#%%
objeto = "Hola"
print(objeto)
def funcion():
    objeto = 2
    print(objeto)
funcion()
print(objeto)
#aqui la funcion crea su propio espacio de nombres, por lo que es diferente la variable objeto sola que la que esta dentro de la funcion 
#%%
#otros ambitos
#globals:busca un dato por afuera de la funcion
#local:regresa el contenido del ambito local pero tipo dict
def ambitos():
    lista = [1, 2, 3]
    nulo = None
    print('Espacio de nombres en el ámbito local:')
    print('%s\n%s\n' %(locals(), dir()))
    print('----------------')
    print('Espacio de nombres en el ámbito global:')
    print(globals())
ambitos()
dir()
#%%
nombre = "Juan"
def nombre_global():
    global nombre
    nombre = "Hola"
print(nombre)
nombre_global()
print(nombre)
