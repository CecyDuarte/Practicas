# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:29:17 2020

@author: almac
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#%%
#generando graficas de funciones
X = np.linspace(-np.pi,np.pi,300,endpoint = True) 

#aplicar semo a cada elemento de mi array
seno = np.sin(X)
coseno = np.cos(X)

#crear un lienzo
plt.figure(figsize=(10,5))
#ahora si lo grafico
plt.plot(X, seno, color="red", linewidth=2, linestyle="dashed", label="Seno")
plt.plot(X, coseno, color="blue", linewidth=1, linestyle=(0,(1,1)), label="Coseno")

#%%
#Estableciendo limites 
plt.plot(X,seno,color = "red",linewidth = 2, linestyle = "dashed", label = "Seno") 
plt.xlim(X.min() * 1.2, X.max() * 1.2) + plt.ylim(coseno.min() * 1.1, coseno.max() * 1.1)
#%%
#control de etiquetas de los ejes
plt.xticks([-np.pi,-np.pi / 2,-np.pi / 4, 0,np.pi / 4,np.pi / 2,np.pi])
plt.yticks([-1,-0.5,0,0.5,1])
#metodologia por capas
#%%
#Compatibilidad de Jupiter con Markdown
plt.xticks([-np.pi,-np.pi / 2,-np.pi / 4, 0,np.pi / 4,np.pi / 2,np.pi],
          [r"$-\pi$",r'$-\pi/2$',r'$-\pi/4$',r'$0$',r'$\pi/4$',r'$\pi/2$',r'$\pi$'])
plt.yticks([-1,-0.5,0,0.5,1],["a","b","c","d","e"])
#%%
#pongo graficas
plt.plot(X,seno,color = "red",linewidth = 2, linestyle = "--",label="Seno")
plt.plot(X,coseno,color = "blue",linewidth = 1, linestyle = "-",label="Coseno")
#de donde a donde las graficas
plt.xlim(X.min() * 1.2, X.max() * 1.2)
plt.ylim(coseno.min() * 1.1, coseno.max() * 1.1)
#Stick eje x
plt.xticks([-np.pi,-np.pi / 2,-np.pi / 4, 0,np.pi / 4,np.pi / 2,np.pi],
          [r'$-\pi$',r'$-\pi/2$',r'$-\pi/4$',r'$0$',r'$\pi/4$',r'$\pi/2$',r'$\pi$'])
#nos crea una leyenda donde nos aparezca seno y coseno
#loc=mejor locacion de letrero
#frame on para poner o no un recuadro
plt.legend(loc = "best",frameon = True)
#%%
#area debajo de la curva
#coloreado
#alpha=trasnparencia
#el coloreado va desde seno hasta coseno, donde coseno>seno
plt.fill_between(X,seno,coseno,coseno>seno,color = "blue",alpha = 0.5)
plt.plot(X,coseno,color = "blue",linewidth = 1, linestyle = "--",label="Coseno")
plt.plot(X,seno,color = "red",linewidth = 1, linestyle = "-",label="Seno")
#%%
#subgraficos:como un array de graficas
X1 = np.linspace(0,5,20)
Y1 = np.exp(X1)
Y2 = - (X1 ** 2)

plt.subplot(2,1,1)
plt.plot(X1,Y1,color = "red",linewidth = 1, linestyle = "--")
plt.yticks(list(range(0,148)))

plt.subplot(2,1,2)
plt.plot(X1,Y2,color = "blue",linewidth = 1, linestyle = (0, (1, 10)))
plt.xticks([1,2,3])
#%%
#Metodo por orientacion a objetos
x = np.linspace(-np.pi,np.pi,20)
#uno solo lienzo de una columna con tres filas, con tamaño indicado, subplots te devuelve dos objetos
x = np.linspace(-np.pi,np.pi,20)
fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (18,5))
#Graficar 1
axes[0].plot(x, x**2, x**3+x)
#titulo de gráfica
axes[0].set_title("Funciones polinomiales")
axes[0].set_xlabel("tiempo")
axes[0].legend(loc = "best", frameon = False)

axes[1].plot(x,(x**2)/(x+1))
axes[1].set_title("Funciones racionales")
#crea un texto en lenguaje latex
axes[1].text(0,0,r"$\frac{x^2}{x+1}$",fontsize=20)

axes[2].plot(x,np.cos(x),x,np.sin(x))
axes[2].set_title("Funciones trigonométricas")
axes[2].set_xlim([-2*np.pi , 2*np.pi])

print(fig)
#%%
#Exportacion e importar el gráfico
#fig es donde guarde el dibujo
fig.savefig("C:/Users/almac/Desktop/ciencia de datos/mis graficos.jpg")
#%%
#importacion
import matplotlib.image as mpimg
#%%
#imread lee y con shape las procesa
impg=mpimg.imread("C:/Users/almac/Desktop/ciencia de datos/mis graficos.jpg")
#tarea que significa el 3er parametro de shape
print(impg.shape)

#%%
import matplotlib.ticker as mtick
#%%
#Personalizacion de graficos
data=pd.read_csv("C:/Users/almac/Desktop/ciencia de datos/GuerrerosZ/kc_house_data.csv")
np.random.seed(2020)
df = data.sample(100)
print(df.head())

#%%
#Precios de casas
x=df["sqft_living"]
y=df["price"]

fig, axes=plt.subplots(figsize=(10,6))
#scatter, es una forma muy usual de analisis exploratorio al ser una grafica de puntos
axes.scatter(x,y, color="blue")
#%%
#spines me sirve para manipular las lineas del cuadro
#quitame la visibilidada
axes.spines["top"].set_visible(False)
axes.spines["left"].set_visible(False)
print(fig)
print(df.head())

#%%
axes.set_title("Tamaño de la casa en $ft^2$ vs precio",fontsize = 20)
axes.set_xlabel("Tamaño",fontsize=15)
axes.set_ylabel("Precio",fontsize=15)
print(fig)
#%%
#pido que manipule el formato de los ejes
y_format="${x:,.2f}"
y_tick=mtick.StrMethodFormatter(y_format)
axes.yaxis.set_major_formatter(y_tick)
fig
#%%
x_format = r"{x:,.0f} $ft^2$"
x_tick = mtick.StrMethodFormatter(x_format)
axes.xaxis.set_major_formatter(x_tick)
fig
#%%
axes.scatter(x,y, s=200,marker = "+",color = "#FF5733",alpha=0.8)
fig
#%%
axes.grid(color = "grey",linestyle="-",linewidth = 0.25,alpha=0.5)
fig
#esto es para que cambiar las lineas a gris
#%%
#x=tam, y=precio, marker en bolitas
#tome el no. de baños y las tonalidades son que tanto y el eje y el precio casa
axes.scatter(x,y,s=400,marker = "o",c=df["bathrooms"],cmap="Reds",alpha=0.8)
fig
#%%
#diagramas de burbuja
axes.scatter(x,y,s=300, c = df["bathrooms"], marker = "o",cmap = "Reds",alpha=0.8)
axes.scatter(x,y,color = "red")
fig
#%%
corr = round(np.corrcoef(x,y)[0][1],2)
print(corr)

#%%
axes.scatter(x,y,s=150, marker = "*",color = "black",alpha=0.5,label=f"Correlación = {corr}")
axes.legend(fancybox=True,prop={"size":14},loc="best")
#propiedades
fig
#tarea como borrar por capas
