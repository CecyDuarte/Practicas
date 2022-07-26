rm (list=ls())
library(nycflights13)
library(tidyverse)

###un TIBBLE es un dataframe arreglado para tidyverse
##dbl numeros decimales
##dttm fechas con horas y minutos
##lgl logicos
##fctr factores
##date  fecha sin horas

##filter() filtrar observaciones de valores concretos
##arrange() reordenar filas de un tibble
##select() seleccionar variables por su nombre
##mutate() crear nuevas variables con funciones a partir de las variables ya existentes
##summarise() colapsa varios valores para dar un resumen estadístico de los mismos

##group_by()  opera la función a la que acompaña grupo a grupo

summary(factor(flights$month))
#como saber cuantos vuelos por cada día del año

vuelos_prueba<-data.frame(fecha=paste(flights$month,flights$day,sep= "_"),flights)

summary(vuelos_prueba$fecha)

vuelos_cumple_cecy<-vuelos_prueba[vuelos_prueba$fecha=="5_30",]
may30<-filter(flights,month==5,day==30) # = y == son simbolos diferentes, el segundo hace un comparativo

##& (y) y | (o)

#dame vuelos que no ocurrieron en mes de enero, abril, mayo y diciembre
filter(storms, wind >= 50, storm %in% c("Alberto", "Alex", "Allison")) 
#la sintaxis VAR %int% c(a,b,c) equivalente a VAR==a| VAR==b| VAR==c

filter(storms, wind >= 50)
help(filter)

exactos<-filter(flights, dep_delay==0)

p<-ggplot(data=exactos)
p + geom_point(mapping =aes(x=carrier,y=arr_delay))

#ordenar de menor a mayor
head(arrange(flights,dep_delay),10)

#ordenar de mayor a menor
arrange(flights,desc(dep_delay))

#varios parámetros
arrange(flights,dep_delay,month)

#selecciones:SELECT

select(flights,dep_delay,arr_delay) # selecciona columnas
select(flights,dep_delay:arr_delay) #selecciona desde dep_delay hasta arr_delay
select(flights,-(year:day)) #selecciona todo excepto desde year hasta day

select(flights,starts_with("dep"))
select(flights,ends_with("delay"))
select(flights,contains("dep"))

##expresiones regulares
select(flights,matches("(.)\\1")) # para usar expresiones regulares
#es un enunciado que tiene sentido para R
select(flights,num_range("x",1:5)) #selecionará las columnas con nombre x1,x2,x3,x4,x5

select(flights,starts_with("dep"),everything())
##me devuelve lo que tenga dep al principio y despues todo lo demás

#rename: solo para renombrar
rename(flights,deptime=dep_time)

#mutate: creación de nuevas columnas
flights_nuevo<-select(flights,
                      year:day,
                      ends_with("delay"),
                      air_time
                      )
mutate(flights_nuevo, time_gain=arr_delay-dep_delay)
help("mutate")
##funciones que aceptan mutate y transmutate
## siempre tiene que ser funciones vectorizadas
## es decir que trabajas con vectores

##funciones acumulativas:
#cumsum(),cumprod,cummin()
#además en dlypr existe cummean()

#rankings: min_rank()







