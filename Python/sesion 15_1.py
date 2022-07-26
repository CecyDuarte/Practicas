# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:56:48 2020

@author: almac
"""
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sns
#ploty crea graficos interactivos 
#%%
#al igual que las otras librerias tiene tablas predeterminadas
#Templates:patrón a seguir
#'ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark', 'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none'
df = px.data.tips()
df.head()
#%%
#Color maps:mapa de colores    
# qualitative, sequential, diverging, cyclical, colorbrewer, cmocean, carto
px.colors.qualitative.swatches()
#%%
#Histogram
px.histogram(data_frame=df
     , x="tip"
     , title="Tip Distribution"
     , template='ggplot2'
     )
#%%
#Stacked Histogram
px.histogram(data_frame=df
             , x="tip"
             , color='sex'
             , barmode = 'group'
             , labels={'tip':'Tips'}
             , title="Tip Distribution : Count of Tips"
             , template='plotly'
            )
#clasificación por color
#%%
#Faceted Histogram:histogramas en facetas,hombres y mujeres
px.histogram(data_frame=df
             , x="tip"
             , color='sex'
             , width=800, height=400
             , facet_row='sex'
             , labels={'count':'Count of Tips'}
             , title="Tip Distribution : Count of Tips"
             , template='plotly_white'
             )

#%%
#Bar Chart:grafica de barras
px.bar(data_frame=df
       , x='day'
       , y='tip'
       , width=800, height=400
       , template='plotly_white'
       , title='Distribution of Tips by day'
      )
#%%
#Boxplot:diagrama de cajas
px.box(data_frame=df
    , y="total_bill"
    , width=800, height=600
    , points="all"
    , color="smoker"
    , notched=False   
    , title="Distribution of Total Bill"
    , template='presentation'
    )
#%%
#Split Box Plot
px.box(data_frame=df
        , y="tip"
        , color="day"
        , title="Distribution of tip by day"
        , template='presentation'
        )
#%%
#Violin Plot
px.violin(data_frame=df
          , y="tip"
          , box=True
          , points="all"
          , title="Distribution of Tips"
          , template='presentation'
         )
#%%
#Split Violin Plot
px.violin(df
        , y="tip"
        , width=800, height=400
        , color="day"
        , box=True
        , title="Distribution of Tips by day"
        , template='presentation'
       )
#%%
#Scatter Plot: de puntos
px.scatter(data_frame=df
           , x="tip"
           , y="total_bill"
           , width=800, height=400
           , trendline='ols'  #ordinary least squares:minimos cuadrados
           , title='Total Bill vs Tips'
           , hover_name='day'
           , labels={'tip':'Tips USD', 'total_bill': 'Total_bill USD'}
           , template='presentation'
          )
#%%
#Scatter Matrix
px.scatter_matrix(data_frame=df
                  , dimensions=["total_bill", "tip", "size"] 
                  , color="sex"
                  , symbol="day" 
                  , title='Attributes Comparison'
                  , hover_name='sex'
                  , template='seaborn'
                 )

iris = px.data.iris()
px.scatter_matrix(iris,
                  dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
                  color="species")
#%%
#Scatter with Marginal Plots
px.scatter(data_frame=df
           , x="tip"
           , y="total_bill"
           , color="sex"
           , title='Total bill vs Tips | by sex'
           , marginal_x='histogram'
           , marginal_y='box'
           , hover_name='sex'
           , opacity=0.8
           , template='seaborn'
          )
#%%
#Heat Map
px.density_heatmap(iris, x="sepal_width", y="sepal_length", marginal_x="histogram", marginal_y="histogram", color_continuous_scale=px.colors.sequential.Hot)
#%%
#Update axes: ves pero mas separados los datos
(px.bar(df, x="size", y="tip", facet_row="time", facet_col="day", 
   color="sex", title="Tips by Payer Sex, Party Size, Day and Meal")
      .update_traces(marker_line_width=0.5)
      .update_yaxes(tickprefix="$")
      .update_layout(title_font_size=30))