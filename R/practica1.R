sin(2*pi)
BD<-data.frame("Num_lista"=c(1,2,3,4),"Nombre"=c("Hugo","Paco","Luis","Conchita"),"Apellido"=c("García","Rulfo","Hilbert","Alonso"))
solver_equation <- function(a,b,c){
  x1 <- (-b - sqrt(b^2-4*a*c+0i))/(2*a)
  x2 <- (-b + sqrt(b^2-4*a*c+0i))/(2*a)
  c(x1,x2)
}
solver_equation(1,2,1)

solver_equation_adv <- function(a,b,c){
  
  if(a == 0){return("El primer argumento debe ser diferente de 0")}
  
  if(Im(solver_equation(a,b,c)[1]) == 0 & Im(solver_equation(a,b,c)[2]) == 0) 
  {as.numeric(unique(solver_equation(a,b,c)))}
  else{
    unique(solver_equation(a,b,c))}
  
}
solver_equation_adv(1,-2,5)
x<-c(1,4,5,3,4,5,2,7,8,9,6)
unique(x)
summary(x) #hace resumen estadistico
base<-data.frame(
  "Entidad"=c("01","01","02"),
  "UPM"=c("002","002","101"),
  "vivienda"=c("10","10","10"),
  "hogar"=c("05","05","07"),
  "renglon"=c("01","02","01"))
viviendas<-paste(base$Entidad,base$UPM,base$vivienda, base$hogar,sep="")
viviendas
