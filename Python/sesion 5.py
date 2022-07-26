# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:37:31 2020

@author: almac
"""

#%%
#declaraciones condicionales
#Script que ejemplifica el uso del condicional if.
   #Si se ingresa un texto igual a "gato", se desplegará el mensaje "miau"."""
#input es para ingresar datos
animal = input("¿Qué animal es? ")
if animal == "gato":
    print("miau")
print ("Sólo los gatos maullan.")

#%%
#if else &elif
#elif es situacion alterna al if
#else en caso de que ninguna de las elif o if venga esa condicion
animal = input("¿Qué animal sugiere? ")
print("Este animal es %s." % animal)
if animal == "gato":
    print("miau")
elif animal == "perro":
    print("guau")
elif animal == "pez":
    print ("glub glub")
elif animal == "gallo":
    print("kikiriki")
elif animal == "vaca":
    print("muuu")
else:
    print("No sé que ruido hace este animal.")
print("Sólo los gatos maullan.")

#%%
#condicionales anidados
dato_texto = input('Ingrese un número entero: ')
dato = eval(dato_texto)
if type(dato) is int:
    print('Es un entero.')
    if dato < 0:
        print('Es negativo.')
    elif dato > 0:
        print('Es positivo.')
    else:
        print('Es cero')
else:
    print('No es un entero.')

#%%
#while
entrada = ""
suma = 0
while suma < 3 and entrada != "despedida":
    entrada = input("Clave: ")
    suma += 1
    print("Intento %d. \n " % suma)
print("Utilizaste %d intentos." % suma)
#%%
#interrumpciones del bloque
#continue
entrada = ""
suma = 0
fallido = 0
while suma < 3:
    suma += 1
    print("Intento %d." % suma)
    entrada = input("Clave: ")
    print()
    # Al ingresar "despedida", se evita que la variable fallido se incremente.
    if entrada == "despedida":
        continue  
    fallido += 1
print("Tuviste %d intentos fallidos." % fallido)
#este hace que no se corte el ciclo aunque ya haya ingresado despedida
#para que si o si ejecute el programa 3 veces

#%%
#break
suma = 0
while suma < 3:
    entrada = input("Clave:")
    #Si se ingresa la palabra "despedida, se termina el ciclo.
    if entrada == "despedida":
        break
    suma = suma + 1
    print("Intento %d. \n " % suma)
print("Tuviste %d intentos fallidos." % suma)

#%%
#exit: termina ejecucion y cierra programa
entrada = ""
suma = 0
while suma < 3:
    entrada = input("Clave:")
    if entrada == "despedida":
        break
    elif entrada == "termina":
        exit()
    suma = suma + 1
    print("Intento %d. \n " % suma)
print("Tuviste %d intentos fallidos." % suma)