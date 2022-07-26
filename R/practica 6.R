library(tidyverse)
rm(list = ls())
##si A es un dataframe, entonces t(A) siempre es una matriz
## si A es un dataframe y lo quieres pasar a tibble utilizamos la función as_tibble()

view(iris)
iris_tibble<-as_tibble(iris)

##crear tibble a partir de vectires individuales

tibble(x=1:5,y=pi,z=y*x^2)

#Función tribble, creas tibble manualmente
tribble(
  ~x,~y,~z,
  "a",5,2.3,
  "b",4,3.2
)
#si quiero convertir un tibble a data frame 
#uso as.data.frame(nombretibble)

## si se quiere más docimentación se puede usar Vignette
vignette("tibble")

###importación de datos:readr
##Sintaxis rea_TIPO ("dirección/nombre")
##lectura de ficheros csv: read_csv (R básico utiliza read.csv)
##lectura de ficheros con separador: read_csv2 
##lectura de ficheros con separador tabulado: read_tsv 
##lectura de ficheros con separador general:read_delim("dirección/nombre", delim= "%)

#sintaxis:write_csv(mpg=file="direccion de csv")

##función parse: convierte tecto y archivos en expresiones
#as de cuenta que le digo procesalo de esta forma
##función eval evalua expresiones
# the string
str <- "1+1"
# A string is not an expression.
is.expression(str)
eval(str)
# parse convert string into expressions
parsed.str <- parse(text="1+1")
is.expression(parsed.str)
eval(parsed.str)

parse_logical(c("TRUE", "FALSE, NA", "TRUE", "hola"))
#el warning me dice que no sabe como tratar el NA y hola
parse_integer(c("21", "3", "hola", "3.14"))

##guess_parser()
#te muestra que tipo de dato es

guess_parser(c("TRUE", "FALSE"))
guess_parser(c("TRUE", "FALSE", "HOLA"))

desafio<-read_csv(readr_example("Challenge.csv"))
#readr_example, le digo que me busque donde esta porque esta ya viene en tidyverse, pero no se donde me la guardo
#marca error porque es una tabla muy grande y se va a fijar en que tipo de datos son cada uno
#pero solo en los primeros 1000 renglones
#por lo que todos los demás te los pone como NA

desafios1<-read_csv(
  readr_example("challenge.csv"),
  col_types = cols(
    x=col_double(),
    y=col_character()
  )
)

#haven lee archivos SPSS, stata, y SAS
#readxl para .xls y .xlsx
#DBI (RMySQL, RSQLite, RpostgratesSQL, etc )





