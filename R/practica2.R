rm ( list = ls())
library(foreign)#para leer y abrir archivos dbf
#dbf:archivo de base de dato
getwd()#dice dirección donde trabajas
setwd("C:\\Users\\almac\\OneDrive\\Documentos\\Cursos\\ciencia de datos\\ejercicios\\ENVIPE-2019-master")#sirve para dirigirme a un lugar especifico de trabajo
#Para direcciones doble diagonal o diagonal invertida
getwd()

tmod_vic1<-read.dbf("Tmod_Vic1.dbf")
tmod_vic2<-read.dbf("Tmod_Vic2.dbf")

tmod_vic<-rbind(tmod_vic1,tmod_vic2) #aqui uno las dos tablas, una abajo de otra. Deben tener igual dimension
dim(tmod_vic)#me dice la dimensión
names(tmod_vic)#nombre columnas
#en este caso, en el PDF, viene a qe se refiere cada columna

ent_nombres<-c("Aguascalientes",
"Baja California",
"Baja California Sur",
"Campeche",
"Coahuila",
"Colima",
"Chiapas",
"Chihuahua",
"Ciudad de México",
"Durango",
"Guanajuato",
"Guerrero",
"Hidalgo",
"Jalisco",
"Estado de México",
"Michoacán de Ocampo",
"Morelos",
"Nayarit",
"Nuevo León",
"Oaxaca",
"Puebla de Zaragoza",
"Querétaro",
"Quintana Roo",
"San Luis Potosí",
" Sinaloa",
"Sonora",
"Tabasco",
"Tamaulipas",
" Tlaxcala",
"Veracruz Llave",
"Yucatán",
"Zacatecas")
tmod_vic$FAC_DEL<-as.numeric(tmod_vic$FAC_DEL) #el signo de pesos arrastra la columna 
ent_ocurrencia<-as.data.frame(tapply(tmod_vic$FAC_DEL,list(tmod_vic$BPCOD,tmod_vic$BP1_2C),sum)[,1:32])
del_nombres<-c("Robo total de vehichulo","Robo parcial de vehiculo","Vandalismo","Robo en casa",
               "Robo en calle","Robo en forma distita a las anteriores","Fraude Bancario",
               "Fraude al consumidor","Extorsión", "Amenazas","Agresión física","Secuestro",
               "Agresión sexual","Violación sexual","otros delitos")
row.names(ent_ocurrencia)<-del_nombres #nombro mis filas
colnames(ent_ocurrencia)<-ent_nombres #nombro columnas

#esta tabla me interesa hacerla para hombres y mujeres
ent_hombres<-tapply(tmod_vic$FAC_DEL,list(tmod_vic$BPCOD,tmod_vic$BP1_2C,tmod_vic$SEXO),sum)[,1:32,1]
#como mi numero de datos de discriminacion son de 3 variables, me devuelve un dataframe de 3 dimensiones
row.names(ent_hombres)<-del_nombres #nombro mis filas
colnames(ent_hombres)<-ent_nombres #nombro columnas

ent_mujeres<-tapply(tmod_vic$FAC_DEL,list(tmod_vic$BPCOD,tmod_vic$BP1_2C,tmod_vic$SEXO),sum)[,1:32,2]
#como mi numero de datos de discriminacion son de 3 variables, me devuelve un dataframe de 3 dimensiones
row.names(ent_mujeres)<-del_nombres #nombro mis filas
colnames(ent_mujeres)<-ent_nombres #nombro columnas

#voy a sacar cada una de mis columnnas de la tabla que he construido
separador<-function(x){
  x<-data.frame("tipo_delito"=del_nombres,x)#has un dataframe donde la primer columna sea tipo delito y segunda columna vector x
  x
  }
#la fn lapply sirve para aplicar una misma función a un conjunto de vectores
#devuelve una lista de la misma longitud del numero de vectores de una colección
#sintaxis(lapply(colección,x))
A<-lapply(ent_ocurrencia,separador)#cuando tomo un lapply lo aplico a dataframe, lo va a aplicar a cada una de las columnas
class(A)
length(A)
#para acceder a listas es doble corchete
View(A[[32]])#los elementos de una lista con corchetes
B<-lapply(ent_hombres,separador)
C<-lapply(ent_mujeres,separador)

pegado<-function(a,b,c){
  #rbind:pegar filas encima de otras;cbind:cuando quiero pegar dataframe de derecha a izquierda
  x<-cbind(a,b[,2],c[,2])
  x<-rbind(x,NA) #para que pegue fila vaciía para poner totales
  x[16,2:4]<-colSums(x[1:15,2:4],na.rm=TRUE) #dado que tiene NA, con na.rm le digo que me los quite y no tome en cuenta
  #colSums, admite NA, colsum, no la admite, es más poderosa la primera
  x<-x[order(-x[,2]),]#ordenamelas por la segunda columna de x
  #order:ordena de menor a mayor, para que lo haga alreves le pones signo menos
  x
}
#mapply, es lo mismo que un lapply pero permite aplicar a varias colecciones 
#sintaxis: napply(función,coleccion1,coleccio2,...,coleccionN,SIMPLIFY=)
#para aplicar esta función deben tener mismo numero de elementos
#simplify=TRUE or FALSE, FAlSE;si se que va a dar un dataframe, si dejas en TRUE;R va adecidir como devolvertelo
u<-pegado(A[[1]],B[[1]],C[[1]])
lista<-mapply(pegado,A,B,C,SIMPLIFY=FALSE)
armado<-function(a){
  a<-data.frame(a[,1],NA,a[,2],NA,NA,NA,a[,3],NA,NA,NA,a[,4])
  #este es para ent_ocurrencia
  a[1,2]<-a[1,3]#mover total a la izquierda
  a[1,3]<-NA#vacia 
  a[,4]<-a[,3]*100/a[1,2]#para que ponga relativos en la columna de alado
  
  #este es para hombres
  a[1,6]<-a[1,7]#mover total a la izquierda
  a[1,7]<-NA#vacia 
  a[,8]<-a[,7]*100/a[,3]
  
  #este es para mujeres
  a[1,10]<-a[1,11]#mover total a la izquierda
  a[1,11]<-NA#vacia 
  a[,12]<-a[,11]*100/a[,3]
  a
}
lista<-lapply(lista,armado)
presentar<-function(a,b){
  a[,1]<-as.character(a[,1])#primer columna convierte en palabras
  a[1,1]<-b
  a[2:16,3][is.na(a[2:16,3])]<-201920192019 #el asignarle ese valor se conoce como bandera
  #ya que como queremos trabajar con los datos en Excel necesitamos que no todos los elementos 
  #sean del mismo tipo
  #is.na[vector]:sirve para identificar los NA, devuelve TRUE or FALSE
  a[2:16,7][is.na(a[2:16,7])]<-201920192019
  a[2:16,11][is.na(a[2:16,11])]<-201920192019
  
  a[2:16,4][is.na(a[2:16,4])]<-202020202020
  a[2:16,8][is.na(a[2:16,8])]<-202020202020
  a[2:16,12][is.na(a[2:16,12])]<-202020202020
  a<-rbind(a,NA)
  a
}
lista<-mapply(presentar,lista,ent_nombres,SIMPLIFY =FALSE)
help(do.call)
#do.call: tomas una función y se lo aplicas a una lista generalmente
#muy parecido a un lapply
tabulado<-do.call(rbind,lista)

#imprimir en Excel
library(xlsx)
wb<-createWorkbook(type="xlsx")#acabo de crear un libro de Excel
hoja<-createSheet(wb,sheetName="Tabulador Rstudio")

#crear un estilo de formato de columnas
#los del ###, es que por cada 3 numeros tengo un espacio
#el + se utiliza para escribir en varias lineas el mismo comando
#esto es solo para los valores absolutos
Abscol<-CellStyle(wb,dataFormat=DataFormat("### ### ###")) +
  Font(wb,color = "Black",heightInPoints = 8,name="Arial") + Fill(foregroundColor = "White") #el fondo blanco

#esto es para valores relativos
Relcol<-CellStyle(wb,dataFormat=DataFormat("0.00")) +
  Font(wb,color="Black",heightInPoints = 8,name="Arial") + Fill(foregroundColor = "White")
#columna de titulos o entidades
Entcol<-CellStyle(wb) +
  Font(wb,color="Black",heightInPoints = 8,name="Arial") + Fill(foregroundColor = "White")

tabulado.abs<-list("2"=Abscol,"3"=Abscol,"6"=Abscol,"7"=Abscol,"10"=Abscol,"11"=Abscol)#pongo el no. de columna entre comillas
tabulado.rel<-list("4"=Relcol,"8"=Relcol,"12"=Relcol)
tabulado.ent<-list("1"=Entcol)

addDataFrame(tabulado,hoja,col.names = FALSE,rownames=FALSE,startRow = 10,startColumn =1,colStyle = c(tabulado.ent,tabulado.abs,tabulado.rel))

saveWorkbook(wb,"tabla_rstudio_clase.xlsx")

