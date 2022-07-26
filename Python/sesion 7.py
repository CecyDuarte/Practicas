# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:25:41 2020

@author: almac
"""
#%%
#Captura de varios argumentos en un parametro de tipo tuple(*args)
#posible definir un parametro que guarde un numero indeterminado de argumento en objeto de tipo tupla
#para esto basta con definir el nombre del arumento con un asterisco antes de
def promedio(*muestras):
    '''Calcula el promedio de la muestra correspondiente a todos los parámetros ingresados.'''
    promedio = sum(muestras)/len(muestras)
    print('El promedio de la muestra de %d elementos es %.3f.' %(len(muestras), promedio))
promedio(1, 3, 5, 8, 11, 24, 90, 29)
promedio(14, 38, 1)
#%%
#el parametro puede tener más de 2 argumentos
def promedio(titulo, *muestras):
    '''Calcula el promedio de la muestra correspondiente a todos los parámetros ingresados con excepción
       del primero, el cual será utilizado como título.'''
    promedio = sum(muestras)/len(muestras)
    print(titulo)
    print('El promedio de la muestra de %d elementos es %.3f.' %(len(muestras), promedio))
promedio('Conteo de abejas en campo.', 34, 45, 61, 23, 47, 41, 52)
promedio(1, 3, 5, 8, 11, 24, 90, 29)
#%%
#Captura de varios argumentos en un parametro de tipo dict(**kargs)
def superficie(**dato):
    '''Calcula la superficie de una figura geométrica si los parámetros  ingresados
       coinciden.'''
    print(dato)
    if dato["tipo"] == "Rectángulo":
        superficie = float(dato["base"]) * float(dato["altura"])
    elif dato["tipo"] == "Triángulo":
        superficie = float(dato["base"]) * float(dato["altura"]) / 2
    elif dato["tipo"] == "Círculo":
        superficie = float(dato["radio"]) ** 2 * 3.14259265
    else:
        print("No puedo calcular la superficie.")
        superficie = "indefinido"
    print("La superficie del %s es de %s" % (dato["tipo"].lower(), superficie))
superficie(base=22, altura=30, tipo="Rectángulo")
superficie(tipo="Círculo", radio = 35)
superficie(base=22, altura=30, tipo="Rombo")
superficie(base=22, altura=30, tipo="Rectángulo", radio=6)
#este dato es parecido a un diccionario, en cuanto a que tiene claves y valores, en donde va a ir compararndo los valores de acuerdo a las claves

#%%
#funciones que regresan valores y cerraduras
#return
def promedio(*muestras):
    return len(muestras), sum(muestras) / len(muestras)
    print(sum(muestras))
promedio(1, 3, 5, 8, 11, 24, 90, 29)
media = promedio(1, 3, 5, 8, 11, 24, 90, 29)
print(media)
print('El promedio de la muestra de %d elementos es %.3f.' %(media))

#%%
"""
class NombreDeLaClase:
    def metodo1(self):  -->todos los métodos de la clase toman "self" como su primer argumento
        #definición  del método
    
    def metodo2(self):
        #definición del método
        
"""
#clases: nos ayudan a programar nuestros propios objetos

class CarroBásico:
    #estas son atributos de la clase
    def girar_izquierda(self):
        #self hace llamar a CarroBásico, y siempre se utiliza
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        #para que no me marque error al tener un atributo sin propiedades
        pass
    
    def frenar(self):
        pass
        
print(CarroBásico)
#me dice que es un objeto de tipo CarroBásico
#%%
"""Las clases se pueden considerar como plantillas que se pueden usar para 
generar objetos. Los objetos generados por una clase se conocen como instancias.
Por ejemplo, CarroBásico nos da las instrucciones para fabricar un coche."""

monchito = CarroBásico()
print(monchito)
#me imprime el tipo y su ubicacion 
type(monchito)
#monchito es una instancia de CarroBásico, o de tipo CarroBásico
#%%
""" Como monchito es una instancia de CarroBásico, tiene sus métodos"""
#aqui mando a llamar los metodos definidos en CarroBásico
monchito.girar_izquierda()
monchito.girar_derecha()
monchito.acelerar()
monchito.frenar()

#%%

""" 
Al igual que con las funciones, generalmente vamos a querer que nuestros objetos
tengan características variables. Con la clase CarroBásico todos nuestros carros
serán 100% iguales. Pero qué pasa si queremos que nuestros carros tengan un color.
Para ello usamos el método especial __init__ que se ejecuta cuando se instancia una clase
"""

class CarroConColor:
    def __init__(self,color):
        self.color = color # Esto es un atributo
    def describir(self):
        print(f"Carro de color {self.color}")
    
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass    
    
#%%
        
monchito_rojo = CarroConColor(color = "rojo") 

monchito_rojo.describir()   

#%%

"""
También podemos añadir atributos a las instancias
"""

monchito_rojo.matricula = "ABC123"

monchito_rojo.matricula

#%%
"""Al crear un CarroConColor sí o sí debemos especificar el color"""

monchito_sin_color = CarroConColor()
#aqui nos marca error por no definir un color
#ya que esta dentro del init, todo lo de afuera como lo anterior no es obligatorio

#%%

"""
Podemos evitar esto simplemente usando valores por defecto en el método __init__"""

class CarroConColor:
    def __init__(self,color = "negro"):
        self.color = color # Esto es un atributo
        
    def describir(self):
        print(f"Carro de color {self.color}")
    
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass    


monchito_sin_color = CarroConColor()

monchito_sin_color.color
monchito_sin_color.describir()

#%%

"""
También podemos definir todas las variables que necesitamos para definir un objeto
"""

class CarroVariable:
    def __init__(self,modelo, velocidad_maxima, color = "negro"):
        self.color = color # Esto es un atributo
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el carro está detenido
        
    def describir(self):
        descripcion = f"Carro modelo {self.modelo} de color {self.color} con velocidad máxima de {self.velocidad_maxima} km/h"
        return descripcion
    
    def estado(self):
        if self.velocidad == 0:
            print("El carro está detenido")
        else:
            print(f"El carro va a {self.velocidad} km/h")
    
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass    
    
#%%    
monchito = CarroVariable(modelo = "Bora", velocidad_maxima = 250, color = "plateado")

monchito.describir()
monchito.estado()
#aqui le cambio el valor del atributo
monchito.velocidad = 120
monchito.estado()

#%%
"""
Uno de los principales usos de las clases es conservar el "estado actual" de un objeto. 
"""

class Carro:
    def __init__(self,modelo, velocidad_maxima, color = "negro"):
        self.color = color # Esto es un atributo
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el carro está detenido
        
    def describir(self):
        descripcion = f"Carro modelo {self.modelo} de color {self.color} con velocidad máxima de {self.velocidad_maxima} km/h"
        return descripcion
    
#    def __repr__(self):
#        return self.describir()
    
    def estado(self):
        if self.velocidad == 0:
            print("El carro está detenido")
        elif self.velocidad > 0:
            print(f"El carro va a {self.velocidad} km/h")
        else:
            print(f"El vehículo va marcha atrás a {-self.velocidad} km/h")
            
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Subiendo la velocidad en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad + diferencia_velocidad
            self.velocidad = min(self.velocidad,self.velocidad_maxima)
        else:
            print("No se puede acelerar negativamente")
            
    def frenar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Frenando en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad - diferencia_velocidad
            self.velocidad = max(self.velocidad,-5)    
    
#%%
        
monchito = Carro(modelo = "Bora", velocidad_maxima = 250, color = "plateado")


monchito.velocidad = -5

monchito.estado()

monchito.acelerar(-300) 

monchito.estado()

monchito.acelerar(50)

monchito.estado()

monchito.frenar(-10)

monchito.frenar(10)

monchito.estado()

monchito.frenar(100)

monchito.estado()

#%%

"""
Herencia de clases
Una de las principales ventajas de usar clases es que se pueden crear otras clases utilizando las ya creadas. Se dice que
una clase hereda a la otra.
Esto nos permite crear una clase genérica después crear clases mas avanzadas con funcionalidades específicas
"""

class Autobús(Carro):
    def acelerar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Subiendo la velocidad en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad + diferencia_velocidad
            self.velocidad = min(self.velocidad,100)
        else:
            print("No se puede acelerar negativamente")
            
    def frenar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Frenando en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad - diferencia_velocidad
            self.velocidad = max(self.velocidad,0)
