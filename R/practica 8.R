rm(list = ls())
library(nycflights13)
library(tidyverse)

flights2<- flights %>%
  select(year:day,hour,origin,dest,tailnum,carrier)

airlines

flights2 %>%
  left_join(airlines, by="carrier") 
#le aumenta una columna de aerolineas
#y pega nombre aerolineas

#claves, identificadores, ID o llaves
#hallar una clave para flights
#si mi identificador me devuelve tibble vacía ya la hice
airports %>%
  count(faa) %>%
  filter(n>1)

#uniones de transformacion
x<-tribble(
  ~key,~val_x,
  1,"x1",
  2,"x2",
  3,"x3"
)
y<-tribble(
  ~key,~val_y,~val_z,
  2,"y1","z1",
  1,"y2","z2",
  4,"y3","z3"
)
#existen 4 tipos de uniones X transformación
##inner_join
x %>%
  inner_join(y,by="key")
x %>%
  inner_join(y[,c(1,2)],by="key")
#devuelve todas las filas donde hay valores coincidentes en y todas las columnas de y
#si hay varias coincidencias, devuelve combinacion de coincidencias

x %>%
  left_join(y,by="key")
#muy parecido a inner_join, solo que las filas sin coincidencias tendran valor de NA
#llevate la información de y para x

x %>%
  right_join(y,by="key")
#la información de x llevate la la tabla y

x %>%
  full_join(y,by="key")
#encima las dos
