# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:27:09 2021

@author: almac
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.offline as ply

from plotly.offline import plot

#%%
#Mapas de colores

fig=px.colors.qualitative.swatches()
plot(fig)

#me va a abrir una pestaña donde aparezca el gráfico interactivo
#%%
df=px.data.tips()
Mi_histograma=px.histogram(data_frame=df, x="tip", title= "Tip Distribution", template="ggplot2")
plot(Mi_histograma)