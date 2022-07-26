rm(list=ls())
library(nycflights13)
library(tidyverse)

flights2<- flights %>%
  select(year:day,hour,origin,dest,tailnum,carrier)

flights2 %>%
  left_join(airlines,by="carrier")

#FAMILIAS DE OPERACION ENTRE TABLAS RELACIONALES:
#UNIONES DE TRANSFORMACIONES
#UNIONES DE FILTRO
#OPERACIONES DE CONJUNTOS

x<-tribble(
  ~llave,~val_x,
  1,"x1",
  2,"x2",
  3,"x3"
)

y<-tribble(
  ~llave,~val_y,~val_z,
  2,"y1","z1",
  1,"y2","z2",
  4,"y3","z3"
)

#definiendo columnas clave
vuelos2<-flights %>%
  select(year:day,carrier,tailnum,origin,dest)

vuelos2 %>%
  left_join(weather)#buena identificación del cientifico de datos
vuelos2 %>%
  left_join(planes,by="tailnum")

##comparativos de los join con R basico y SQL
##dplyr             merge
##inner_join(x,y)   merge(x,y)
##left_join(x,y)   merge(x,y,all,x=TRUE)
##right_join(x,y)   merge(x,y,all,y=TRUE)
##full_join(x,y)   merge(x,y,all,x=TRUE,all,y=TRUE)

##dplyr                    SQL
##inner_join(x,y,by="z")   SELECT *FROM x INNER JOIN y USING (z)
##left_join(x,y,by="z")   SELECT *FROM x LEFT OUTER JOIN y USING (z)
##right_join(x,y,by="z")   SELECT *FROM x RIGHT OUTER JOIN y USING (z)
##full_join(x,y,by="z")   SELECT *FROM x FULL OUTER JOIN y USING (z)

##semi_join(x,y) MANTIENE todos los renglones en x con coincidencias en y
##anti_join(x,y) DESCARTA todos los renglones en x con coincidencias en y
vuelos3<- flights %>%
  left_join(airports[c(1,2)],by=c("dest"="faa")) #voy a jalar el nombre de los destinos

#cuales son los destinos más populares ordenados de mayor a menor
destinos_populares<-vuelos3 %>%
  count(name,sort=TRUE) %>%
  head(10) #se queda con primeros 10

vuelos3 %>%
  filter(name %in% destinos_populares$name) 
#cada vez que te encuentres un nombre de los vuelos3, hazme un filtrado en los vuelos populares
#si es alguno de los destinos populares filtrame la tabla

vuelos3 %>%
  semi_join(destinos_populares)#mismo filtrado que anteriores
#a diferencia de los anteriores, no estoy aumentando información de la tabla
#estoy echandole un clavado

#información de vuelos que no son populares
vuelos3 %>%
  semi_join(destinos_populares)

##operaciones entre conjuntos
df1<-tribble(
  ~x,~y,
  1,1,
  2,1
)

df2<-tribble(
  ~x,~y,
  1,1,
  1,2
)
intersect(df1,df2) #nombre columnas debe ser el mismo

union(df1,df2)
setdiff(df1,df2) 
setdiff(df2,df1)
#la diferencia no es commutativa







