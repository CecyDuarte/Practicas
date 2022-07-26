# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:04:59 2020

@author: almac
"""

#%%Estructuras
"""Sets:Conjunto de elementos donde no hay repeticiones
#sus elemntos son de tipo inmutables
#la funcion set() ingresa un objeto iterable a tipo set
"""
grupo_amigos1 = set(["Manuel","Rodrigo","Miguel","Jesús","Hugo"])
grupo_amigos2 = {"Manuel","Alejandro","Fernando","Antonio","Luis"}

print(type(grupo_amigos1)) 
print(type(grupo_amigos2))

print(grupo_amigos1)
"""los conjuntos no admiten los objetos repetidos
#siempre te da los datos ordenados
#diferencia entre set y tupla, si admite objetos iguales la tupla
"""
#%%
#podemos ver que elementos hay en el conjunto
"Manuel" in grupo_amigos1
"Rodrigo" in grupo_amigos2
#%%
"""operaciones entre conjuntos
Unión de conjuntos: set1.union(set2)
"""
print(grupo_amigos1.union(grupo_amigos2))
# Observar que este método no cambia al set como tal
print(grupo_amigos1)

# Intersección de conjuntos: set1.intersection(set2)
print(grupo_amigos1.intersection(grupo_amigos2))
print(grupo_amigos1&(grupo_amigos2))

"""Diferencia de conjuntos: set1.difference(set2) o bien set1-set2
#Quienes estan en el primero sin que esten en el grupo 2
"""
diferencia1 = grupo_amigos1.difference(grupo_amigos2)
diferencia2 = grupo_amigos1 - grupo_amigos2
#aqui es lo mismo pero con metodos diferentes
print(diferencia1)
print(diferencia2)
# Diferencia simétrica: set1.symmetric_difference(set2)
#son cosas que estan en un conjunto pero que no estan en el otro conjunto, excluye la intersección
print(grupo_amigos1.symmetric_difference(grupo_amigos2))
"""los conjuntos no los podemos mandar a llamar por sus indices como en listas y tuplas
si son recorribles por le for
Reemplazos:
    
        Operación	reemplazo    
    set1.union(set2)	set1.update(set2)
set1.intersection(set2)	set1.intersection_update(set2)
set1.difference(set2)	set1.difference_update(set2)
set1.symmetric_difference(set2)	set1.symmetric_difference_update(set2)
es decir, que si quiero realizar una operacion y que sustituya el resultado en el conjunto
una vez que use la funcion de reemplazamiento, ya no puedo recuperar el objeto
"""
#%%
#Operaciones internas
guerreros_z = {"Gokú","Vegueta","Krilin","Yamcha","Ten Chin Han","Pikoro","Gohan"}
print(guerreros_z)
# Añadir un elemento: set1.add(<objeto nuevo>)
guerreros_z.add("Trunks")
#el metodo add añade de uno en uno 
print(guerreros_z)
#Y si el elemento que queremos añadir ya existe, no hace nada nuevo
#%%
# Quitar un elemento: set1.remove(<objeto a quitar>). Si no lo encuentra, enviará un error
guerreros_z.remove("Yamcha")
print(guerreros_z)
guerreros_z.remove("Yamcha")
print(guerreros_z)
#si no tengo el elemento va a llorar
#Para evitar ese error, utilizamos un equivalente que lo busca y, si no lo encuentra, no hace nada.
#%%
# Quitar un elemento y si no lo encuentra no marcar error: set1.discard(<objeto a quitar>)

guerreros_z.discard("Ten Chin Han")
print(guerreros_z)
guerreros_z.discard("Ten Chin Han")
print(guerreros_z)
#estos metodos lo hacen de uno por uno

#%%
#comparacion de conjuntos
saijajines = {"Gokú","Vegueta","Gohan","Trunks"}
# Son conjuntos disjuntos? set1.isdisjoint(set2), no tienen elementos en comun?
print(saijajines.isdisjoint(guerreros_z))
# Es el conjunto 1 un subconjunto del conjunto 2? set1.issubset(set2)
#el conjunto es subconjunto del conjunto
print(saijajines.issubset(guerreros_z))
#%%
#Esta instrucción admite otra sintaxis "natural"

# set1 < set2
#aqui nos pregunta si es subconjunto
print(saijajines < guerreros_z)
# Es el conjunto 1 un superconjunto del conjunto 1? set1.issuperset(set2)
#el conjunto 1 contiene al conjunto 2
print(guerreros_z.issuperset(saijajines))
# Son el conjunto 1 y el conjunto 2 iguales? set1 == set2
print(guerreros_z == saijajines)
#SE PUEDEN GRAFICAR CONJUNTOS COMO DIAGRAMAS DE VENN, PERO ESO ES PARA MÁS AVANZADO
#%%
from collections import Counter
#lo de arriba es una importacion de libreria
lista=["a", "b","c", "d"]
resumen=Counter(lista)

print(resumen)
print(type(resumen))
#es un objeto parecido a los diccionarios
#por lo que podemos acceder a sus elementos mediante las claves, en caso de no encontrar la clave, devuelve 0
print(resumen["a"])
print(resumen["d"])
#podemos ir añadiendo claves
resumen.update("d")
#podemos añadir un recuento al objeto counter con un diccionario
resumen.update({"b":5,"e":9})
#añade 5 b & 9e
print(resumen)
resumen.update({"b":-5,"e":2})
#quita 5 b & añade 2 e
print(resumen)
#%%
#podemos especificar ademas el recuento de un elemento
resumen=["e"]=1
print(resumen)
#los counter & arrays no son nativos de Python, hay que agregar librerias

#%%
#Input & Output
import os
#Creacion de carpetas
os.makedirs("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta", exist_ok = True)
#no se puede crear un archivo que ya existe
#pero con exist_ok = True, me la vuelve a crear, pero borra si es que ya existe
#%%
#pero en nuevas versiones ya no pasa esto
os.listdir("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta")
#devuelve elementis que tenga en esta carpeta
#%%
#leer y escribir archivos
"""Podemos usar open para abrir archivos. Si el archivo no existe, dará un error.

archivo_inexistente = open("RUTA DONDE ESCRIBIREMOS EL ARCHIVO/NOMBRE DEL ARCHIVO A ABRIR.EXTENSIÓN")
Si queremos crear un archivo para escribir, debemos especificar argumento "w"

archivo_para_escribir = open("RUTA DONDE ESCRIBIREMOS EL ARCHIVO/NOMBRE DEL ARCHICO A ABRIR.EXTENSIÓN","w")
"""
archivo_para_escribir=open("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta/sesion8.txt","w")
archivo_para_escribir.write="hola mi amor"
archivo_para_escribir.close()
#nunca abras el archivo si lo estas modificando, puede llegar a hacer cosas raras en el sistema
"""Para escribir en él usamos el método write.

archivo_para_escribir.write("hola mundo.") 
"""
archivo_para_escribir.write="¿Cómo están todos?"

#Y no se escribe nada hasta que lo cerremos.

archivo_para_escribir.close()


"""Si usamos el argumento "w", reescribiremos el archivo
"""
archivo_para_escribir = open("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta/sesion8.txt","w")

archivo_para_escribir.write("Bienvenidos a CDD_Py de SciData.")

archivo_para_escribir.close()


"""Podemos usar el método "a" para escribir sin borrar el original
"""
archivo_para_escribir = open("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta/sesion8.txt","a")
archivo_para_escribir.write("\nEsperamos que les guste el curso.")
archivo_para_escribir.close()


"""Usar el método de open-close no es ideal, pues si ocurre un error entre los dos estados podemos perder o dañar el archivo original.

La manera más recomendable es usando "with"
"""
#%%
guerreros_z = ["Gokú","Vegueta","Krilin","Yamcha","Ten Chin Han","Pikoro","Gohan"]

with open("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta/usuarios.txt","w") as archivo_para_escribir:
    for guerrero in guerreros_z:
        archivo_para_escribir.write(f"{guerrero} ")

#Si quisieramos escribir cada elemento en un renglón diferente solo añadimos el \n
#%%
with open("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta/usuarios2.txt","w") as archivo_para_escribir:
    for guerrero in guerreros_z:
        archivo_para_escribir.write(f"{guerrero}\n")
"""
#Investigar que otros tipos de archivo puede abrir_tarea
#%%
#Lectura
También podemos leer archivos muy fácilmente.
"""
#%%
with open("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta/usuarios.txt") as archivo_para_leer:
    datos = archivo_para_leer.read()

print(datos)

type(datos)

#Si queremos leer cada línea del archivo por separado, usamos el método readlines(), que va leyendo de forma iterativa (y consume menos memoria)

cada_linea = []

with open("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta/usuarios.txt") as archivo_para_leer:
    lineas = archivo_para_leer.readlines()
    for linea in lineas:
        cada_linea.append(linea.strip("\n"))

print(lineas)
print(cada_linea)
type(lineas)
type(cada_linea)
#%%
"""

#Escritura de tablas csv a partir de un diccionario.
gt6#algo muy usual para la creacion de base de datos
"""
#Los archivos csv son una forma de almacenar datos con cada columna separada por una coma.

#Por ejemplo, tomemos el diccionario

#{"nombre":["Antonio","Miguel","Julian","Andres"],"edad":[45,40,22,34],"ciudad":["Ciudad de México","Puebla","Mexicali","Aguascalientes"]}

"""Dicho diccionario en csv se vería como

nombre,edad,ciudad

Antonio,45,Ciudad de México

Miguel,40,Puebla

Julián,22,Mexicali

Andrés,34,Aguascalientes

En Python, es posible escribir archivos csv a partir de diccionarios:
"""
datos = {"nombre":["Antonio","Miguel","Julian","Andres"],
         "edad":["45","40","22","34"],
         "ciudad":["Ciudad de México","Puebla","Mexicali","Aguascalientes"]
         }

claves = list(datos.keys())
n_items = len(datos[claves[0]])
#%%
with open("C:/Users/almac/OneDrive/Documentos/Cursos/ciencia de datos/Cecycarpeta/DiccionarioACSV.csv", "w") as nombre_archivo:
    nombre_archivo.write(','.join(claves)+"\n")
    for i in range(n_items):
        fila = ",".join([str(datos[clave][i]) for clave in claves])
        nombre_archivo.write(fila+"\n")
