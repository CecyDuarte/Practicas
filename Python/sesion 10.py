# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:12:05 2020

@author: almac
"""

#%%
#PANDAS
#tablas 
import pandas as pd
import numpy as np

#%%
#series: tips arrays de una dimension
serie_1 = pd.Series(np.random.rand(8))
print(serie_1)

#%%
serie_1=pd.Series(np.random.rand(8),name="mi primer serie")
print(serie_1)
print(serie_1[4])
#%%
serie_2=pd.Series(np.random.rand(8),index=range(1,9),name="mi segunda serie")
print(serie_2)
#%%
serie_3=pd.Series(np.random.rand(5),index=[4,6,1,2,8])
print(serie_3)
print(serie_3[0])
print(serie_3[4])
#%%
serie_4=pd.Series(np.random.rand(5),index=["a","e","i","o","u"])
print(serie_4)       
#%%
diccionario={"Nombre":["Hector", "Manuel"], "Apellido":"Garduño"}
print(pd.Series(diccionario))
                       
#%%
#Dataframes
#arreglos de 2 dimensiones, como una tabla
#las columnas pueden ser de diferente tipo
print(pd.DataFrame(data=[(0,1,2), (1,2,3), (2,3,4),(3,4,5)]))
#%%
estudiantes={"Nombre":["Hugo", "Paco", "Luis", "Pedro", "Juan", "Pablo"],
             "Apellido":["Lopez", "Silva", "Oca", "Ramirez", "Guitierrez", np.nan],
             "Matricula":["123455", "736923", "971298", "123098", "987656", "878652"],
             "Edad:":[20,35,30,25, np.nan, 23]}
print(estudiantes)
print(pd.DataFrame(estudiantes))
#%%
matriz=np.arange(9).reshape(3,3)
print(matriz)
print(pd.DataFrame(matriz))
#%%
registro=("1a persona", "2a persona", "3a persona", "4a persona", "5a persona", "6a persona")
print(pd.DataFrame(data=estudiantes, index=registro))
#%%
matriz=np.arange(9).reshape((3,3))
print(pd.DataFrame(matriz, index=["uno", "dos", "tres"], columns=["a", "b", "c"]))
#%%
print(pd.DataFrame(
    [["Hugo", "Lopez", 123455, 20], 
    ["Paco", "silva", 736923, 35], 
    ["Luis", "Oca", 123098],
    ["Pedro", "Ramirez", 971298]
    ], index=["Registro 1", "Registro 2", "Registro 3", "Registro 4"],
    columns=["Nombre", "Apellido", "Matricula", "Edad"]
    ))
#%%
estudiantes=pd.DataFrame(
    [["Hugo", "Lopez", 123455, 20], 
    ["Paco", "silva", 736923, 35], 
    ["Luis", "Oca", 123098],
    ["Pedro", "Ramirez", 971298]
    ], index=["Registro 1", "Registro 2", "Registro 3", "Registro 4"],
    columns=["Nombre", "Apellido", "Matricula", "Edad"]
    )
print(estudiantes)
print(estudiantes["Nombre"])
print(estudiantes[["Nombre", "Edad"]])
#acceso fila con nombre
print(estudiantes.loc[["Registro 2", "Registro 4"]])
#acceso fila por no. indice
print(estudiantes.iloc[1])
#ciertas filas y columnas
print(estudiantes.loc[["Registro 1", "Registro 4"]][["Matricula", "Edad"]])
#%%
#operaciones basicas
estudiantes["Nombre completo"]=estudiantes["Nombre"]+""+ estudiantes["Apellido"]
print(estudiantes)
#agregas columna o campo
#%%
"eliminando columnas"
estudiantes.drop("Nombre completo", axis=1, inplace=True)
#axis: columna 1 y 0 fila, inplace: true o false, si quiero que sustituya objeto
print(estudiantes)
#%%
#indexar numericamente registros

estudiantes.reset_index(inplace=True)
print(estudiantes)
#los indices anteriores los convierte a nueva columna, y los nuevos indices son numericos
#%%
#Acceso a ciertos columnas y ciertas filas
print(estudiantes.loc[[0,3], ["Matricula", "Edad"]])
#%%
#filtrado
print(estudiantes[estudiantes["Edad"]>20][["index", "Edad", "Matricula"]])
#%%
#cambiando nombres de las columnas
estudiantes.columns=["Campo 1", "Campo 2", "Campo 3", "Campo 4", "Campo 5"]
print(estudiantes)
#%%
estudiantes.index=estudiantes["Campo 4"]
print(estudiantes)
#%%
#agregando elemento
nuevo_elemento="Registro 5, Helena, Gonzalez, 888888, 29"
nuevo_elemento.split(", ")
estudiantes.loc[88888]=nuevo_elemento.split(",")
print(estudiantes)
#%%
print(estudiantes.iloc[-1])
#loc va a buscar la posicion
#%%
#Visulaizar encabezado y cola
print(estudiantes.head(3))
#los ultimos dos registros
print(estudiantes.tail(2))
#%%
estudiantes["Campo 5"] = pd.to_numeric(estudiantes["Campo 5"], downcast = "float")
#convierte el dato a flotante
print(estudiantes)
print(estudiantes["Campo 5"].mean())
#%%
print(estudiantes["Campo 5"].value_counts())
#es como una tabla de frecuencias
#%%

estudiantes.loc[777222] = ["Registro 6","José","López","777222",30]
print(estudiantes)
#ahora si lo ingresas como entero
#%%
print(estudiantes["Campo 3"].value_counts())
#como Gonzalez lo meti con split, viene espacio con el rebanado
#%%
#ordenamiento en forma desscendente
estudiantes.sort_values(by = "Campo 5",inplace = True, ascending=False)
print(estudiantes)
#false si es descendente, true si es ascendente
#%%
#para sacar la media
edad_media=estudiantes["Campo 5"].mean()
print(int(edad_media))
#%%
estudiantes["Campo 5"].fillna(int(edad_media), inplace=True)
print(estudiantes)
#%%
estudiantes.sort_index(ascending=True, inplace=True)
print(estudiantes)
#ordenamientos por indices
#%%
#ordenar por varias columnnas
estudiantes.sort_values(by=["Campo 3", "Campo 5"], ascending=[True,False], inplace=True)
print(estudiantes)
#%%
print(estudiantes[estudiantes["Campo 3"]=="Lopez"])
#%%
estudiantes["Campo 2"]=estudiantes["Campo 2"]. str.upper()
print(estudiantes)
#hace mayusculas
#%%
print(estudiantes["Campo 4"].str.len())
#longitudes
#%%
estudiantes.loc["536271"] = ["Registro 7","Luisa","González","536271","23"]
estudiantes["Estado"] = ["Activo","Baja","Baja","Graduado","Activo","Activo","Baja"]

print(estudiantes)
#añadir nueva fila y columna
#%%
#columnas dummies
print(pd.get_dummies(estudiantes["Estado"]))
#estoy desagrupando informacion
#%%
Frame = pd.concat([estudiantes,pd.get_dummies(estudiantes["Estado"])],axis = 1)
print(Frame)
#juntar dataframe
#%%
Frame["Fac"]=[4,3,1,4,5,1,8]
Frame["Sexo"]=["0","1","1", "1", "1","1","0"]
print(Frame)
#%%
print(Frame.groupby("Estado")["Fac"].sum())
#%%
print(Frame.groupby(["Estado", "Sexo"])["Fac"].sum())
#%%
print(Frame.groupby(["Estado", "Sexo"])["Fac"].sum()["Activo", "0"])

#%%
#esta es muy importante
print(Frame.describe())
#%%
print(Frame["Sexo"].describe())

