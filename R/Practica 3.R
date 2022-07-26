#Tidyverse:univero ordenado
#Los paquetes incluidos en Tidyverse tienen como objetivo cubrir todas las fases de la Ciencia de datos dentro de R: importar datos, ponerlos en formato ordenado (tidy), buscar relaciones entre ellos (mediante su transformación, visualización y creación de modelos) y comunicar los resultados.
#Además de los paquetes principales que realizan estas funciones, al instalar el Tidyverse también se proporcionan otros que ayudan a trabajar con fechas, cadenas de caracteres o factores siguiendo los mismos principios.
library(tidyverse)
rm ( list = ls())
#si usas filter() no voy a saber si es de dplyr o stats
#por eso el conflicto
#aplica lo mismo para el otro conflicto
#gglot2,tiene bases de datos como mpg 
help(mpg)
view(mpg)
#descripción de campos
#cyl:cilindros
#displ: desplazamiento del motor; es una medida del motor
#trans:tipo de transición
#drv:tipo de tracción
#city:millas por galón en la ciudad
#hwy:millas por galón en autopista
#fl:tipo de combustible
##c;d;diesel,...
#class: tipo de carro
summary(mpg$fl)
summary(as.factor(mpg$fl))

p<-ggplot(data=mpg)
#sactterplot:grafica de una nube de puntos
#geometrias de lo que queremos calcular
#si solo pongo data=mpg no me pone nada porque estas construyendo el pizarrón
p + geom_point(mapping = aes(x=displ,y=hwy),data=mpg)
  #aesteticas:lo que quiero representar y como lo quiero representar

p<-ggplot(data=mpg)
p + geom_point(mapping = aes(x=displ,y=hwy,colour=factor(cyl),shape = factor(cyl)),data=mpg)

#agrupa
p<-ggplot(data=mpg)
p + geom_point(mapping = aes(x=displ,y=hwy,alpha=cty),data=mpg)

summary(mpg$cty)
#dividir gráficas por clase
#separa por clases en cuadros
p<-ggplot(data=mpg)
p + geom_point(mapping = aes(x=displ,y=hwy)) +facet_wrap(~class,nrow = 2)

#separa por clases en columnas, en una sola fila
p<-ggplot(data=mpg)
p + geom_point(mapping = aes(x=displ,y=hwy)) +facet_grid(.~class)

#compara los 7 tipos de clasificación por filas
p<-ggplot(data=mpg)
p + geom_point(mapping = aes(x=displ,y=hwy)) +facet_grid(class~.)

p<-ggplot(data=mpg)
p + geom_point(mapping = aes(x=displ,y=hwy)) +facet_grid(class~fl)


##otras geometrias
#geometría suave
p<-ggplot(data=mpg)
p + geom_smooth(mapping = aes(x=displ,y=hwy,linetype=drv,color=drv)) 
p + geom_point(mapping = aes(x=displ,y=hwy,color=drv)) 

########
?diamonds
#Grafica de barras para una sola variable
j<-ggplot(data=diamonds) 
j + geom_bar(mapping=aes(x=cut))

summary(diamonds$cut)
#hacer un table para meter el resume
demo_diamonds<-tribble(
  ~cut,         ~freqs, #creo columnas
  "Fair",       1610,
  "Good",       4906,
  "Very Good",  12082,
  "Premium",    13791,
  "Ideal",      21551
)

view(demo_diamonds)

j<-ggplot(data=demo_diamonds) 
j + geom_bar(mapping=aes(x=cut,y=freqs),stat = "Identity")

j<-ggplot(data=diamonds)
  stat_summary(
    mapping = aes(x=cut,y=price), 
    fun.min=min,
    fun.max=max,
    fun=median
  )

#lo anterior esta en frecuencias absolutas
  #si lo quiero en relativas hago lo siguiente
j<-ggplot(data=diamonds) 
j + geom_bar(mapping=aes(x=cut,y=..prop..,group=1))

#Tarea:
#Investigar en geom_bar con y=..prop.. qué significa el parámetro group

j<-ggplot(data=diamonds) 
j + geom_bar(mapping=aes(x=cut,y=..prop..,group=100))
j + labs(x="Etiqueta x", y="Etiqueta y")

j<-ggplot(mpg,aes(x=cty,y=hwy)) 
j + geom_point()
j + labs(x="Etiqueta x", y="Etiqueta y")

library(maps)

italia<-map_data("italy")
k<-ggplot(data=italia,aes(long,lat,group=group))
k + geom_polygon(fill="blue", color="red")
k + coord_quickmap()