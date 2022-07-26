# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:59:06 2020

@author: almac
"""
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%%
iris_=pd.read_csv("C:/Users/almac/Desktop/ciencia de datos/iris_dataset.csv")
print(iris_.head())
#%%
#Cargando datos con Seaborn
#iris ya viene de la tabla iris
iris = sns.load_dataset("iris")
print(iris.head())

#%%
#grafica de violin
#le digo que columna quiero actualizar
sns.violinplot(x="sepal_length", data=iris)

#%%
#contextos de Seaborn: son templates
# Styles: darkgrid, whitegrid, dark, white, and ticks
sns.set_style("darkgrid")
sns.boxplot(x="species", y="petal_length", data=iris)
#%%
#cuadriculas
sns.set_style("whitegrid")
sns.boxplot(x = "species", y = "petal_length", data=iris)
sns.despine(right=True, top=True)
#pine eran las lineas, los del rectangulo
#despine los quita
#%%
#set_context
#Contextos disponibles: paper, notebook, talk and poster
sns.set_style("ticks")
sns.set_context("paper")
sns.boxplot(x = "species", y = "petal_length", data=iris)
#%%
sns.set_style("ticks")
sns.set_context("poster")
sns.boxplot(x = "species", y = "petal_length", data=iris)
#%%
sns.set_style("whitegrid")
sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.8})
sns.boxplot(x = "species", y = "petal_length", data=iris)
#%%
#admite varios tipos de argumentos
#El set context puede recibir varios parámetros de entrada
sns.set_context("paper", font_scale=1.8, rc={"font.size":5,"axes.labelsize":1.0})
sns.boxplot(x = "species", y = "petal_length", data=iris)
#font_size y axes.labelsize, va modificando el tamaño del cuadro de la gráfica
#%%
#definir un control fijo para futuros graficos
#con fn set, es como crear una configuracion por default
# Parámetros por defecto definidos por el usuario
sns.set(rc={"font.size":6,"axes.labelsize":6})
sns.boxplot(x = "species", y = "petal_length", data=iris)
#%%
# Reset default params
sns.set(palette='Set2')
sns.set_context("notebook")
sns.boxplot(x = "species", y = "petal_length", data=iris)

# Reset default params
sns.set(palette='Set2')
sns.set_context("notebook")
sns.boxplot(x = "species", y = "petal_length", data=iris)
#%%
#Bar Plot
df = sns.load_dataset("iris")
df.head()
fig, axes = plt.subplots(figsize=(6,4))
sns.barplot(x=df["species"], y=df["sepal_length"], palette="pastel",data=df,ax=axes,estimator=np.mean)
#%%
#Boxplot
planets = sns.load_dataset("planets")
planets.head()
sns.set(style="ticks", palette="muted")
ax = sns.boxplot(x="distance", y="method", data=planets)
ax.set_xscale("log")
#%%
#Violin plot
tips = sns.load_dataset("tips")
tips.head()
sns.set(style="whitegrid")
sns.violinplot(x="time",y="total_bill", data=tips, palette="rainbow")
sns.violinplot(x="day",y="total_bill", data=tips, palette="rainbow", hue='sex')
#%%
#Grouped violinplots with split violins
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True,inner="quart",
               palette={"Male": "#33FFF8", "Female": "#FDFF33"})

#%%
#Scatter Plot Matrix: Pairplot () function
sns.pairplot(df, hue="species", palette='cubehelix')
#%%
#Catplot:función general para generar graficos en seaborn
sns.set(style="ticks")
g = sns.catplot("day", "total_bill", "sex", data=tips, kind="box", palette='cubehelix')
g.set_axis_labels("Day", "Total Bill")
#%%
#FaceGrid
sns.set(style="ticks")
g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill", color='red')

#%%
#Cambiar el tamaño del gráfico in Seaborn
g = sns.FacetGrid(tips, col="smoker", col_order=["Yes", "No"], height=4, aspect=1)
g.map(plt.hist, "total_bill", color="green")

#%%
#Cambiar paletas de colores
kws = dict(s=40, linewidth=.5, edgecolor="w")
#s=size,col=columna, hue=clasificación, hue_order=colorear por cierto orden
g = sns.FacetGrid(tips, col="sex", hue="time", palette="Set2", hue_order=["Dinner", "Lunch"])
g = g.map(plt.scatter, "total_bill", "tip", **kws).add_legend()
#%%
#Use different marker for the hue levels
palette = dict(Lunch="blue", Dinner="red")
g = sns.FacetGrid(tips, col="sex", hue="time", palette=palette,
                  hue_order=["Dinner", "Lunch"],
                  hue_kws=dict(marker=["^", "v"]))
g = g.map(plt.scatter, "total_bill", "tip", **kws).add_legend()

#%%
#Use different axes labels after plotting
g = sns.FacetGrid(tips, col="smoker", row="sex")
g = g.map(plt.scatter, "total_bill", "tip", color="g", **kws).set_axis_labels("Total bill (USD)", "TIP")