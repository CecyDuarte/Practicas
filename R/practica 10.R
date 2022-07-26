rm(list=ls())
##familia de funciones apply

library(tidyverse)
df<-tibble(
  a=rnorm(10),
  b=rnorm(10),
  c=rnorm(10),
  d=rnorm(10)
)
#hace ciclos, notación de ::sirve para aquellas funciones que marque conflicto
purrr::map_dbl(df,sum)

##map() crea una lista
##map_lgl() crea un vector lógico
##map_dbl() crea un vector númerico
##map_int() crea un vector con entradas enteras
##map_chr() crea un vector con entradas "palabras"

df %>%
  map_dbl(prod)

##MODELOS LINEALES
  library(modelr)
ggplot(sim1,aes(x=x,y=y)) +
  geom_point() +
  geom_abline(aes(intercept=5,slope=2),color="red") 
#graficador de lineas rectas
#pendiente=2

#propondremos un modelo lineal de la forma y=a0+a1*x

modelos<-tibble(
  a1=runif(250,-20,40),
  a2=runif(250,-5,5)
)

head(modelos)

ggplot(sim1,aes(x=x,y=y)) +
  geom_point() +
  geom_abline(aes(intercept=5,slope=2),color="red") +
  geom_abline(aes(intercept=a1,slope=a2),data=modelos,alpha=0.25)

model1<-function(a,data){
  #a es un vector
  #b es un dataframe
  a[1]+a[2]*data$x
}

model1(c(7,1.5),sim1)

measure_distance<-function(mod,data){
  diff<- data$y - model1(mod,data) #hace diferencia
  sqrt(mean(diff^2)) #raiz de la suma al cuadrado de diferencias
}

measure_distance(c(5,2),sim1)

sim1_dist<-function(a1,a2){
  measure_distance(c(a1,a2),sim1)
}

modelos<-modelos %>%
  mutate(dist=purrr::map2_dbl(a1,a2,sim1_dist))

ggplot(sim1,aes(x,y)) +
  geom_point(size=2,color="grey30") +
  geom_abline(
    aes(intercept=a1,slope=a2,color= -dist),
    data=filter(modelos,rank(dist)<3) #devuelve rectas con mejor aproximación
  )

#el metodo de optim
#usa el metodo de Newton-Rapson, pra saber el valor de a1 y a2
#cuyos valores minimicen el error
#aqui le das un valor inicial

best<-optim(c(0,0),measure_distance, data=sim1)

best$par #me muestra la mejor pareja de valore

##
sim1_mod<-lm(y~x,data=sim1) #genera modelo y=x 

##
grid<-sim1 %>%
  data_grid(x) #dice entre que valores esta x

grid<-grid %>%
  add_predictions(sim1_mod) #te predice los valores

ggplot(sim1,aes(x)) +
  geom_point(aes(y=y)) +
  geom_line(aes(y=pred),data=grid,color="red",size=1)

sim1<-sim1 %>%
  add_residuals(sim1_mod) #devuelve residuos

ggplot(sim1,aes(resid)) +
  geom_freqpoly(binwidth=0.5)

##model_matrix
df<- tribble(
  ~y, ~x1, ~x2,
  4, 2, 5,
  5, 1, 6
)

model_matrix(df,y~x1)
model_matrix(df,y~ x1 + x2)
model_matrix(df,y~x1+x2^2)

#variables categoricas
df<-tribble(
  ~genero, ~respuesta,
  "masculino", 1,
  "femenino", 2,
  "masculino", 1
)

model_matrix(df,respuesta ~ genero)

ggplot(sim2) +
  geom_point(aes(x,y)) 

mod2<-lm(y~x, data=sim2)

mod2$coefficients

grid<-sim2 %>%
  data_grid(x) %>%
  add_predictions(mod2)

tapply(sim2$y,sim2$x,mean)

ggplot(sim2,aes(x)) +
  geom_point(aes(y=y)) +
  geom_point(data=grid,aes(y=pred),color="red",size=4)
