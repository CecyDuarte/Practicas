# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:13:11 2020

@author: almac
"""

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Distribuciones univariadas
x = np.random.normal(size=100)

#%%
#Histogramas
#kde:para que aparezca o no función de densidad, rug:controla la presencia de alfombras, alpha:transparencia, shade: es para que lo rellene
print(x)
sns.displot(x, kde=True, rug=True, color='green', label='Histogram',alpha=0.5)
plt.legend(loc='best')
sns.kdeplot(x, color='orange',shade=True)
#%%
#Joint Plot:graficas propuestas
#joinplot:junta graficas
# Scatter plot
sns.set(style="white")
tips = sns.load_dataset("tips")
sns.jointplot(x="total_bill", y="tip", data=tips, color="red")

#%%
#Hexbin plots
#modificar estos puntitos
#kind:cambia la visualización
sns.jointplot(x = "total_bill", y = "tip", data=tips, color='green', kind="hex")
# kde plot 2D:dibuja las curvas bivariadas
sns.jointplot(x = "total_bill", y = "tip", data=tips, kind="kde", space=0, color="green")
#%%
iris = sns.load_dataset("iris")
# Scatter plot
#marginal_kws:distribuciones marginales, soy de comer diccionario con bins n no. de barras necesarias
sns.jointplot(x = "petal_length", y = "sepal_length", data=iris,
                  marginal_kws=dict(bins=15),
                  s=40, color='blue', edgecolor="w", linewidth=1,
                 height=5, ratio=5)
iris.head()
#%%
#Fit Linear Regression to data
#se puede hacer regresiones
#kind=reg: me suelta las regresiones
sns.jointplot(x = "sepal_length", y = "sepal_width", data=iris,color='purple', kind="reg", height=6)
# linear regression by multiple pair variables
#pairplot:regresion para varias variables, ya que las pones a pelear las variables
sns.pairplot(iris, kind="reg", height=2, aspect=1.2)
#hace regresión importando especie de cada uno 
sns.pairplot(iris, kind="reg", hue="species", palette="coolwarm", height=2, aspect=1.2)

#%%
#Heat Map
#Correlation matrix
iris.corr()
# si no requieres la barra de color:cbar=False
#fmt:que me ponga a dos decimales
plt.figure(figsize=(8,6))
#mapa de color
ax = sns.heatmap(iris.corr(), annot=True, linecolor='white',linewidths=.3, fmt='.2f', cbar=True, cmap=(sns.color_palette("Blues")))

#%%
#Flights Datase
#se aplica mapa de colores a una cierta matriz
flights = sns.load_dataset("flights")
f = flights.pivot_table(index='month', columns='year', values='passengers')
flights.head()
print(f)
#%%
#Cluster Map:
# dendogram: hierarchical relationship between objects
# The key to interpreting a dendrogram is to focus on the height
# at which any two objects are joined together.
sns.clustermap(f,figsize=(8, 10), cmap='coolwarm', linecolor='white', linewidths=1)