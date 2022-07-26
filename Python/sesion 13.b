# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:56:12 2020

@author: almac
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%%
#Scatter:Grafico de puntos
#edged color es el contorno de puntos
x = np.linspace(-5,5,20)
y = x**2
plt.scatter(x,y, s=200, color='yellow',marker='.',edgecolors='red')
#aqui es la funcion scatter
#%%
#Graficas de barras
classes = ['C1', 'C2', 'C3', 'C4']
colors  = ['#FF5733', '#3533FF', '#33FF5D', '#FDFF33']
#alturas de las barras
numerical = [[10, 15, 5, 7],
             [1, 3, 4, 9],
             [4, 15, 8, 10],
             [7, 6, 13, 8]]
#grupos como claes 
number_groups = len(classes) 
#ancho barras
bin_width = 0.2

fig, axes = plt.subplots(figsize=(8,6))
#.bar es hacer grafica de barra
for i in range(number_groups):                        
    axes.bar(x=np.arange(len(classes)) + i*bin_width,    
           height=numerical[i],
           width=bin_width,
           color=colors[i],
           align='center')

axes.set_xticks(np.arange(len(classes)) + 0.4)
axes.set_xticklabels(classes)
#%%
#histograma
#bins:barras, patches:anchos
np.random.seed(2020)
x = np.random.sample(50)
n, bins, patches = plt.hist(x, bins=20, facecolor='orange', alpha=0.7, density=True)
plt.setp(patches[3], facecolor = 'blue')
plt.xlabel('bins')
plt.ylabel('Values')
#grid las rejas
plt.grid(color='gray', linestyle='-', linewidth=0.25, alpha=0)
#%%
#Grafica de pastel

# Pie chart, where the slices are ordered and plotted counter-clockwise:
labels = 'Segment 1', 'Segment 2', 'Segment 3', 'Segment 4'
sizes = [30, 35, 25, 10]  # percentages, the sum of all of them must to be 100%
resaltado = (0, 0.01, 0, 0)  # only "explode" the 2nd slice (i.e. 'Segment 2')

fig, ax = plt.subplots()
#shadow un contorno, startang angulo que quiero que empiece
ax.pie(sizes, explode=resaltado, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
#para que Python no se vuellva loco

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#%%
#grafico de caja
_high = np.random.rand(20) + 0.5
center = np.random.rand(20)
_low = np.random.rand(20) - 0.5

data = [_high,center,_low]
plt.boxplot(data,notch=False, vert=True, patch_artist=True)
#patch_artist:relleno, vert=vertical
#%%
#Grafico de violin:hermano del de caja
plt.figure(figsize=(9,4))
plt.violinplot(data,widths=0.40, vert=True, showmeans=True, showextrema=True, showmedians=True)
#showmeans:mostrar medias
fig, axes = plt.subplots(figsize=(9, 4))
axes.violinplot(data, widths=0.40, vert=True, showmeans=True, showextrema=True, showmedians=True)
axes.set_title('Violinplot', fontsize=10)
plt.setp(axes, xticks=[i+1 for i in range(len(data))], xticklabels=['high','center','low'])
#%%
#grafico de burbujas
#plt.style.use('ggplot')
df = pd.DataFrame(np.random.rand(50, 3), columns=['x','y','z'])
df.plot(kind='scatter',x='x',y='y',s=df['z']*400, color='red', edgecolors='black')
# s is the size of the bubble
#%%
#3D plots
from mpl_toolkits.mplot3d.axes3d import Axes3D
img = plt.figure()
ax = Axes3D(img)
x = np.arange(-5,5,0.25)
y = np.arange(-5,5,0.25)
X, Y = np.meshgrid(x, y)
V = np.sqrt(X**2 + Y**2)
Z = np.sin(V)
ax.plot_surface(X,Y,Z, rstride=2, cstride=2, cmap='hot',linewidth=0)
#%%
#color bar
p = ax.plot_surface(X,Y,Z, rstride=2, cstride=2, cmap='hot',linewidth=0)
img.colorbar(p, shrink=0.5)
img
# The rstride and cstride parameters help in sizing the cell on the surface.
#%%
fig = plt.figure()
ax = Axes3D(fig)
ax.view_init(elev=50., azim=30)
ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap='hot')
# setting the view at 50 degrees elevation and 30 degrees angle:
fig = plt.figure()
ax = Axes3D(fig)
ax.view_init(elev=50., azim=30)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
#%%
#curvas 3D
fig = plt.figure(figsize=(8,6))
ax = fig.gca(projection='3d')

v = np.linspace(-5 * np.pi, 5 * np.pi, 100)
z = np.linspace(-3, 3, 100)
r = z**2 + 1
x = r * np.sin(v)
y = r * np.cos(v)
 
ax.plot(x, y, z, label='3D curve')
ax.legend(loc='best')