library(tidyverse)
rm(list = ls())
##LIMPIEZA DE DATOS
tabla1<- tribble(
  ~pa�s, 		~a�o, 	~casos,	~poblaci�n,
  "Afganistan",	1999,	745,	19987071,
  "Afganistan",	2000,	2666,	20595360,
  "Afganistan",	2001,	3000,	20595360,
  "Brasil",	1999,	37737,	172006362,
  "Brasil",	2000,	80488,	174504898,
  "Brasil",	2001,	85000,	174504898,
  "China",	1999,	212258,	1272915272,
  "China",	2000,	213766,	12504428583,
  "China",	2001,	220000,	12504428583
)

tabla2<-tribble(
  ~pa�s, 		    	~a�o, 		~tipo,			~conteo,
  "Afganistan",		1999,		"casos",		    745,
  "Afganistan",		1999,		"poblaci�n",		19987071,
	"Afganistan",	  2000,		"casos",		    2666,
	"Afganistan",		2000,		"poblaci�n",		20595360,
	"Brasil",	    	1999,		"casos",		    37737,
	"Brasil",	    	1999,		"poblaci�n",		172006362,
	"Brasil",		    2000,		"casos",		    80488,
	"Brasil",		    2000,		"poblaci�n",		  174504898,
	"China",		    1999,		"casos",		    212258,
	"China",		    1999,		"poblaci�n",		1272915272,
	"China",		    2000,		"casos",	    	213766,
	"China",		    2000,		"poblaci�n",		12804428583
)

rat<- function(x,y){
	x<-as.character(x)
	y<-as.character(y)
	paste(x,y,sep = "/") #con esto lo pongo como fracci�n 
}

tabla3<- tabla1 %>%
	group_by(pa�s,a�o) %>%
	summarise(tasa=rat(casos,poblaci�n))

tabla4a<-tribble(
	~pa�s,		~"1999",	~"2000",
	"Afganistan",	745,		2666,
	"Brasil",	37737,		80488,
	"China",	212258,		213766
)

tabla4b<-tribble(
	~pa�s,		~"1999",	~"2000",
	"Afganistan",	19987071,	20595360,
	"Brasil",	172006362,	174504898,
	"China",	1272915272,	12804428583
)

tabla1 %>%
  mutate(rate=casos/poblaci�n*10000)

tabla1 %>%
  count(a�o,wt=casos)

ggplot(data=tabla1,mapping = aes(x=a�o,y=casos)) +
  geom_line(aes(group=pa�s),color="grey50") +
  geom_point(aes(color=pa�s))

##gather: unir y spread:dispersar
Tabla1<-tabla1
#con t transpongo la tabla
as_tibble(t(as.data.frame(Tabla1)))

tidy4a<-tabla4a %>%
  gather("1999","2000",key = "a�o",value = "casos")

tidy4b<-tabla4b %>%
  gather("1999","2000",key = "a�o",value = "poblaci�n")

tabla4<-left_join(tidy4a,tidy4b)
tabla4

tabla2 %>%
  spread(key=tipo,value = conteo)

##separate() y unite()
#separate:separa en columnas, si es que hay una variable no numerica
#en sepate(), si ocupo sep=VALOR_NUMERICO, entender� que debe separar
#tanto lugares como indica VALOR_NUMERICO. El 1 es el primer simbolo
#de izquierda a derecha y el -1 es el primer simbolo de derecha a izquierda
tabla3 %>%
  separate(tasa,into = c("casos","poblaci�n")) %>%
  separate(poblaci�n,into = c("millones","millares","unidades"),sep=c(-6,-3))

acciones<-tibble(
  a�o=c(2015,2015,2015,2015,2016,2016,2016),
  trimestre=c(1,2,3,4,2,3,4),
  retorno=c(1.88,0.59,0.35,NA,0.92,0.17,2.64)
)

acciones %>%
  spread(key=a�o,value=retorno)

##complete()
#sirve para arreglar problemas de NA

acciones %>%
  complete(a�o,trimestre)

##
tratamiento<-tribble(
  ~sujeto, ~medicina, ~respuesta,
  NA,2,10,
  NA,3,9,
  "Emma",1,4,
  NA,3,NA,
  "Alma",NA,8,
  NA,4,8,
  "amor",1,9
)

tratamiento %>%
  fill(sujeto, .direction="up") #me rellena los espacios

who1<-who %>%
  gather(new_sp_m014:newrel_f65,key="key",value="cases",na.rm = TRUE)

who2<-who1 %>%
  mutate(key=stringr::str_replace(key,"newrel","new_rel"))

who3<- who2 %>%
  separate(key,c("nuevos","tipo","sexo_edad"),sep = "_")

who4<- who3 %>%
  select(-iso2,-iso3,-nuevos)

who5<- who4 %>%
  separate(sexo_edad, c("sexo","edad"),sep=1)
  








