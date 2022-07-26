rm(list = ls())
##resumenes estadísticos: SUMMARY
library(tidyverse)
library(nycflights13)

summarise(flights,retraso=mean(dep_delay,na.rm = T))

##en general no es muy útil
#su fuerza se ve cuando trabajamos agrupaciones

grupo_mes<-group_by(flights,year,month)

class(grupo_mes)
#Tibble, es decir, es un dataframe que esta adaptado para trabajar con dlypr

summarise(grupo_mes,retraso=mean(dep_delay,na.rm = T))
#esto es similar a que si usaramos el tapply

summary(grupo_mes$month)
summary(factor(grupo_mes$month))

tapply(flights$dep_delay,flights$month,function(x)(mean(x,na.rm = T)))
#lo del na.rm=T me elimina los na si es true

##PIPES==tuberías==conexiones
#el simbolo %>% representa una conexión
#esto es lo mismo que: retrasos<-group_by(flights,carrier)
retrasos<-flights   %>% #Tomate la tabla vuelos y 
  group_by(carrier) %>% #Agrupamela por aerolinea
  summarise(median_dep= median(dep_delay,na.rm = T),
            mean_dep=mean(dep_delay,na.rm = T))  %>% 
  #y entonces realizame este resumen estadísticos
  mutate(orden_mediana= min_rank(median_dep),
         orden_media= min_rank(mean_dep))   %>%
  #Y entonces, aplicale un mutate
  arrange(orden_media,
          orden_mediana)
#Y entonces, acomodamelos mediante este criterio

########
por_destino<-group_by(flights,dest) %>%
  summarise(
          count=n(),
          dist = mean(distance,na.rm = T),
          delay = mean(arr_delay,na.rm = T)
          )
#la función count me muestra cuantos vuelos llegaron al aeropuerto

no_cancel<- flights %>%
    filter(!is.na(dep_delay)  | !is.na(arr_delay)) %>%
    group_by(tailnum) %>%
    summarise(delay=mean(arr_delay))

ggplot(data=no_cancel,aes(x=delay)) +
  geom_freqpoly()









