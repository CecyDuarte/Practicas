# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:04:49 2020

@author: almac
"""

import numpy as np
import pandas as pd
#%%
#uniones y concatenacion

df1 = pd.DataFrame({
    "A":["A0","A1","A2","A3"],
    "B":["B0","B1","B2","B3"],
    "C":["C0","C1","C2","C3"],
    "D":["D0","D1","D2","D3"],
})
print(df1)
#%%
df2 = pd.DataFrame({
    "A":["A4","A5","A6","A7"],
    "B":["B4","B5","B6","B7"],
    "C":["C4","C5","C6","C7"],
    "D":["D4","D5","D6","D7"],
})

print(df2)
#%%

df3 = pd.DataFrame({
    "A":["A8","A9","A10","A11","A12"],
    "B":["B8","B9","B10","B11","B12"],
    "C":["C8","C9","C10","C11","C12"],
    })

print(df3)
#%%
#concatenar columnas
df_columnas=pd.concat([df1,df2,df3], axis=0, keys=["df1", "df2", "df3"])
print(df_columnas)
#%%
#mando a llamar 
print(df_columnas.loc["df2"])
#%%
df_filas = pd.concat([df1,df2,df3],axis = 1,keys = ["df1","df2","df3"])
print(df_filas)
#%%
df3.index=[2, 5, 3, 4, 10]   
print(df3)
df_filas = pd.concat([df1,df2,df3],axis = 1,keys = ["df1","df2","df3"])
print(df_filas)
#%%
#joins:conjuntos
izquierda = pd.DataFrame({
    "A":["A0","A1","A2","A3"],
    "B":["B0","B1","B2","B3"],
    "C":["C0","C1","C2","C3"],
    },index = ["clv0","clv1","clv2","clv3"])

derecha = pd.DataFrame({
    "D":["D0","D1","D2","D3","D4"],
    "E":["E0","E1","E2","E3","E4"]
    },index = ["clv0","clv2","clv1","clv5","clv6"])
print(izquierda)
print(derecha)
#no puedes tener dos columnas con el mismo nombre, basta con una, se usaria en lo de join con un rsuffix al final
#o bien usar merge que es muy parecido a join solo que aqui no tendriamos este 
#%%
#columna join es la columna id
izquierda["Id"]=izquierda.index
derecha["Id"]=derecha.index
print(derecha)
print(izquierda)
#%%
join_interno = izquierda.join(derecha.set_index(["Id"]),on = ["Id"],how = "inner")
print(join_interno)
#coincidencia de Id, y jala inf por los Id
#%%
join_izquierdo = izquierda.join(derecha.set_index(["Id"]),on = ["Id"],how = "left")
print(join_izquierdo)
#tarea left join pero sin el inner
#%%
join_derecho = izquierda.join(derecha.set_index(["Id"]),on = ["Id"],how = "right")
print(join_derecho)
#%%
join_completo = izquierda.join(derecha.set_index(["Id"]),on = ["Id"],how = "outer")
print(join_completo)
#%%
#Practica
cuestio1=pd.read_csv("C:/Users/almac/Desktop/ciencia de datos/GuerrerosZ/conjunto de datos/tr_cbasico1.csv")
cuestio2=pd.read_csv("C:/Users/almac/Desktop/ciencia de datos/GuerrerosZ/conjunto de datos/tr_cbasico2.csv")
#%%
socio1=pd.read_csv("C:/Users/almac/Desktop/ciencia de datos/GuerrerosZ/conjunto de datos/tr_csocio1.csv")
socio2=pd.read_csv("C:/Users/almac/Desktop/ciencia de datos/GuerrerosZ/conjunto de datos/tr_csocio2.csv")
socio3=pd.read_csv("C:/Users/almac/Desktop/ciencia de datos/GuerrerosZ/conjunto de datos/tr_csocio3.csv")
#%%
cuestio1.columns[:10]
print(cuestio1.shape)
print(cuestio2.shape)
cuestio1["ID"] = cuestio1["CD_A"].astype(str) + "_" + cuestio1["PER"].astype(str) + "_" + \
                 cuestio1["ENT"].astype(str) + "_" + cuestio1["CON"].astype(str) + "_" + \
                 cuestio1["V_SEL"].astype(str) + "_" + cuestio1["N_HOG"].astype(str) + "_" + \
                 cuestio1["N_REN"].astype(str)
cuestio2["ID"] = cuestio2["CD_A"].astype(str) + "_" + cuestio2["PER"].astype(str) + "_" + \
                 cuestio2["ENT"].astype(str) + "_" + cuestio2["CON"].astype(str) + "_" + \
                 cuestio2["V_SEL"].astype(str) + "_" + cuestio2["N_HOG"].astype(str) + "_" + \
                 cuestio2["N_REN"].astype(str)
#(eval:buscar)tarea buscar donde vea mucho codigo, tratar de disminuir
cuestio = cuestio1.join(cuestio2.set_index(["ID"]),on = ["ID"],how = "inner", rsuffix="copia")
print(cuestio.shape)
#%%

socio1["ID"] = socio1["CD_A"].astype(str) + "_" + socio1["PER"].astype(str) + "_" + \
                 socio1["ENT"].astype(str) + "_" + socio1["CON"].astype(str) + "_" + \
                 socio1["V_SEL"].astype(str) + "_" + socio1["N_HOG"].astype(str) + "_" + \
                 socio1["N_REN"].astype(str)

socio2["ID"] = socio2["CD_A"].astype(str) + "_" + socio2["PER"].astype(str) + "_" + \
                 socio2["ENT"].astype(str) + "_" + socio2["CON"].astype(str) + "_" + \
                 socio2["V_SEL"].astype(str) + "_" + socio2["N_HOG"].astype(str) + "_" + \
                 socio2["N_REN"].astype(str)
socio3["ID"] = socio3["CD_A"].astype(str) + "_" + socio3["PER"].astype(str) + "_" + \
                 socio3["ENT"].astype(str) + "_" + socio3["CON"].astype(str) + "_" + \
                 socio3["V_SEL"].astype(str) + "_" + socio3["N_HOG"].astype(str) + "_" + \
                 socio3["N_REN"].astype(str)
socio = pd.concat([socio1,socio2,socio3])
print(socio)
#%%
#solo me quedo con estas columas
socio = socio[["ID","SEX","EDA","FAC18"]]
print(socio)
#%%
#llevar informacion de socio a cuestionario

print(list(cuestio.columns))
#%%
print(cuestio["FAC"].sum())
#%%
print(cuestio.groupby(["S4P25_3"])["FAC"].sum() )
print(100 * cuestio.groupby(["S4P25_3"])["FAC"].sum() / cuestio["FAC"].sum())
#%%
print(
100 * cuestio[(cuestio["S5P13_1"] == 1) | (cuestio["S5P13_10"] == 1) | (cuestio["S5P13_19"] == 1) | 
(cuestio["S5P13_2"] == 1) | (cuestio["S5P13_11"] == 1) | (cuestio["S5P13_20"] == 1) | 
(cuestio["S5P13_3"] == 1) | (cuestio["S5P13_12"] == 1) | (cuestio["S5P13_21"] == 1) | 
(cuestio["S5P13_4"] == 1) | (cuestio["S5P13_13"] == 1) | (cuestio["S5P13_22"] == 1) | 
(cuestio["S5P13_5"] == 1) | (cuestio["S5P13_14"] == 1) | (cuestio["S5P13_23"] == 1) | 
(cuestio["S5P13_6"] == 1) | (cuestio["S5P13_15"] == 1) | (cuestio["S5P13_24"] == 1) | 
(cuestio["S5P13_7"] == 1) | (cuestio["S5P13_16"] == 1) | (cuestio["S5P13_25"] == 1) | 
(cuestio["S5P13_8"] == 1) | (cuestio["S5P13_17"] == 1) | (cuestio["S5P13_26"] == 1) | 
(cuestio["S5P13_9"] == 1) | (cuestio["S5P13_18"] == 1) | (cuestio["S5P13_27"] == 1)]["FAC"].sum() / cuestio["FAC"].sum())