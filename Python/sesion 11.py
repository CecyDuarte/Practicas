# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:54:20 2020

@author: almac
"""

#%%
import numpy as np
import pandas as pd
airbnd=pd.read_csv("C:/Users/almac/Desktop/ciencia de datos/ejercicios/SciData/airbnb_cdmx.csv")
print(airbnd.head())

#%%
#escritura
df=pd.DataFrame({"Nombre":["a","b", "c"], "Numero": [1,2,3]})
print(df)

df.to_csv("C:/Users/almac/Desktop/ciencia de datos/ejercicios/SciData/DataFrame_sesion11.csv",index=False, header=True, endcoding="latin")
#true or false es para ver si queires que aparezcan
#endcoding: indica que tipo de diccionario para escribir vamos a utilizar
#%%
airbnd=pd.read_csv("C:/Users/almac/Desktop/ciencia de datos/ejercicios/SciData/airbnb_cdmx.csv")
print(airbnd.head())
#%%
#problema de Roberto contra su hermana
problema2=airbnd[(airbnd["id"]==43856289) | (airbnd["id"]==107078)]
print(problema2)

#%%
#Problema 1
"""
noches_disponibles>=6
Num_hab>=2
Num criticas>10
puntuacion >4

ordenar de mayor a menor puntuacion. En caso de empate ordenar por num_criticas descendientes
dividir la tabla en 3 partes iguales

"""""

alicia=airbnd[(airbnd["minimum_nights"]>=6) & (airbnd["bedrooms"]>=2) & (airbnd["number_of_reviews"]>=10) & (airbnd["review_scores_accuracy"]>4)].sort_values(by=["review_scores_accuracy", "number_of_reviews"], ascending=[False, False])

print(alicia)
print(alicia.head(1108))
#%%
print(alicia.iloc[0:round(alicia.shape[0]*0.3)])
#%%
print(alicia.head(round(alicia.shape[0]*0.3)))


