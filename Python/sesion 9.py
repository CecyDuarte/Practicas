# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:24:08 2020

@author: almac
"""

#%%
"""Numpy: es un paquete especializado en la creación, gestión y operación 
(incluyendo funciones matemáticas y estádisitcas básicas y generación de números aleatorios)
 con arreglos de una o varias dimensiones.
 Cabe señalar que Numpy generalmente se beneficia del uso de bibliotecas de algebra lineal 
 escritas en FORTRAN, tales como Lapack, BLAS y OpenBLAS. Incluso existen algunas variantes
 de Numpy diseñadas para realizar cálculos mediante GPU tales como Gnumpy.
Los tipos de datos y los arreglos de Numpy son elemento base del resto de los componentes de Scipy 
e incluso de otras herramientas de cómputo científico.
"""

import numpy as np
#%%
# sintaxis arrays: nombre_del_arreglo = np.array("estructura")
array_1d=np.array([1,2,3])
print(array_1d)
array_2d=np.array([[1,2,3],[4,5,6]])
print(array_2d)
#%%

print(f"El arreglo array_1d tiene un total de {array_1d.ndim} dimensiones, las cuales valen {array_1d.shape} respectivamente, por lo cual cuenta con {array_1d.size} elementos")

print(f"El arreglo array_1d tiene un total de {array_2d.ndim} dimensiones, las cuales valen {array_2d.shape} respectivamente, por lo cual cuenta con {array_2d.size} elementos")
#%%
array_con_nulos=np.array([2,4, np.nan, 8])
#np.nan: intriduce elementos nulos al array
print(array_con_nulos)
array_con_nulos[np.isnan(array_con_nulos)]=0
#para cambiarle el valor nulo le pones np.isnan y le asignas el valor
print(array_con_nulos)
#%%
#Indexado de arrays
mi_arreglo=np.array([[3,4,5,9],
                    [7,8,3,12],
                    [0,3,23,20],
                    [8,11,6,21]])
print(mi_arreglo)
print(mi_arreglo[0,1:3])
#array[fila, columna]
print(mi_arreglo[1, :])
#imprime toda la fila 2
print(mi_arreglo[:,2])
#imprime toda la columna 3
print(mi_arreglo[:, -1])
#imprime toda la ultima columna
#%%
#observacion con el indxado
matriz=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(matriz)

seleccion=matriz[1,1]
print(seleccion)
seleccion=100
print(matriz)

seccion=matriz[:2,]
print(seccion)
seccion[0,0]
seccion[0,0]=100
print(matriz)
#te lo cambia solo cuando estamos trabajando con arrays, y seleccionando el elemento o elementos a cambiar 
#%%
#filtrados
matriz=np.array([[1,4],[2,4],[5,0]])
print(matriz)

matriz_filtrada=matriz>=2
print(matriz_filtrada)
print(matriz[matriz_filtrada])

#%%
#Arrays especiales
#sintaxis: np.function(shape,dtype)
print(np.ones((2,1)))
#por default si no le pones el dtype te arroja elementos de tipo flotante
print(np.ones((4,3),dtype=int))
print(np.zeros((2,1)))
print(np.zeros((4,3)))
#%%
print(np.empty((2,1),dtype=str))
print(np.empty((4,3),dtype=bool))
#%%
#np.arange=funcion que permite crear arreglo de 1 dimension
#np.arange(inicio, fin, incrementos, dtype=<tipo de dato>)
#inicio sera 0 si no dices, incrementos en 1, y el dtype lo inferira
print(np.arange(5,12))
print(np.arange(6.24, 15.2, 0.8))

#%%
#funcion np.linspace
#np.linspace(inicio, fin, num=segmentos, dtype=tipo de dato)
print(np.linspace(0,1, num=11))

#%%
#Modificacion de la forma y tamaño de un arreglo
#np.ravel(), sintaxis: np.ravel(<arreglo>)
#aplanar una array 
arreglo_1=np.array([[1,2,3],
                    [4,0,-5],
                    [-6,7,-8]])
print(np.ravel(arreglo_1))
print(arreglo_1)
#%%
#np.reshaped()
#np.reshape(<arreglo>, <forma>)
arreglo_2=np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]])
print(arreglo_2.shape)
#tenglo que respetar los elemntos dado la tupla
print(np.reshape(arreglo_2,(6,2)))
#%%
#np.resize(), sintaxis:np.resize(<arreglo>, <forma>)
arreglo_3=np.array([[1,2],
                    [3,4]])
print(np.resize(arreglo_3,(3,2)))

#%%
#np.concatenate
arreglo_1=np.array([[1,2],
                    [3,4]])
arreglo_2=np.array([[5,6],
                    [7,8]])
print(np.concatenate((arreglo_1,arreglo_2),0))
print(np.concatenate((arreglo_1, arreglo_2),1))
#%%
#matrices con elementos aleatorios
#paquete np.random, sintaxius: np.random.rand(<forma>)
#crea arreglo cuyos elementos son va´s entre 0 y 1 con dist unif
print(np.random.rand(3,5))
#matriz de 3 filas con 5 columnas
#%%
#np.random.randint(), sintaxis: np.random.randint(<inicio>, <fin>, <forma>)
#arreglo con elementos aleatorios de tipo int
print(np.random.randint(1,3, (3,3)))
print(np.random.randint(0,256, (10, 3)))
print(np.random.randint(0, 256, (3,2,4)))
#no olvida que fin=fin-1
#arreglo de 3 dimensiones

#%%
#Operaciones con arreglos
#matriz identidad
print(np.eye(3))

#%%
#producto puntual de 2 matrices
print(np.array([[1,2,3],[4,5,6]]) * np.array([[0,1,0],[0,0,1]]))

A = np.array([[1,4,3],[2,5,1]])
print((A >= 3 ) * A)

#%%
#Producto usual de matrices
A=np.array([[1,4,3], [2,5,1]])
B=np.array([[2,3,1,0], [5,5,1,0],[4,1,2,0]])
print(A@B)
print(f"La forma de A es {A.shape}; la de B es {B.shape}. Por lo tanto la de AB es {(A @ B).shape}")

#%%
#el paquete numpy.linalg: biblioteca especializada en algebra lineal con las siguientes funciones
#determinantes
A=np.arange(9).reshape(3,3)
print(np.linalg.det(A))
#%%
#soluciones de ec. lineales con np.linalg.solve()
a=np.array([[2,5,-3],
            [11, -4,22],
            [54,1,19]])
y=np.array([22.2,11.6, -40.1])
print(np.linalg.solve(a,y))

#%%
#Matriz inversa
print(np.linalg.inv(a))
print(np.linalg.inv(a).dot(y))
#el dot, hace la multiplicacion de la inversa con el producto usal de la otra matriz

#%%
#Transpuesta de una matriz
b=np.arange(9).reshape((3,3))
print(b)
print(b.transpose())
print(np.transpose(b))
#uno es una funcion y otra es un metodo