# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 13:27:08 2020

@author: almac
"""
import re
#raw strings: no consideran el signo diagonal como escape
saludo = "Hola\nMundo.\tYa casi terminamos"
print(saludo)
r_saludo = r"Hola\nMundo.\tYa casi terminamos"
print(r_saludo)

#%%
#Match: buscar coincidencias en un string conforme a un patrón
#buscar coincidencias de textos, parecido a mineria de datos
txt = "Expresiones regulares en Python"
coincidencia = re.search('Python', txt)# r is for raw strings
print(coincidencia)#me dice en que lugar lo encontro
#%%
if coincidencia:
    print(f"Hubo coincidencia en la frase '{txt}' con la palabra {coincidencia.group()}")
else:
        print("No hubo coincidencia")
#%%
#Compile: crear un objeto de tipo expresiones regulares
mensaje = "Mi número es 610-742-8645"
mi_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#con la fn compiler;\d cualquier digito [0-9]
res = mi_regex.search(mensaje)#aplico fn search, busca expresion regular en mensaje ya que ya es expresión regular
print(res.group())#imprimo con el group

#%%
#Findall: Encontrar todos los patrones en un string y que devuelva todas las coincidencias
txt = "Expresiones regulares en Python"
resultado = re.findall('e', txt)#encuentra todas las e
print(resultado)#va a ser una lista con todas las e que encontro
result2 = re.findall('en', txt)
print(result2)
result3 = re.findall('[seo]', txt)
print(result3)
message1 = "Mis números son 610-742-8645 y 563-852-9642"
regex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#busca los numero -, va a regresar todas las coincidencias
res1 = regex1.findall(message1)
print(res1)
#las expresiones regulares es principio de minería de datos
#un ejemplo son las nubes de texto
#%%
#Group: to get the matched string
regex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match1 = regex2.search(mensaje)
print(match1)
match1.group()
match1.group(1)
match1.group(2)
#agrupa y los parentesis es para delimitar los grupos
#%%
#Escaping Special Characters
str = 'Sentences have dots.\nHow do we escape them?\n'
lst = re.findall('.', str)#quiere que me busque los puntos
#me devuelve todas las letras, da todos los caracteres a excepción el salto de linea
print(lst)
lst1 = re.findall('\n', str)#regresa los saltos
print(lst1)
#%%
#Pipe Character (|): match one of many possible group
exp = re.compile(r'Py(thon|mysql|charm)')#va a buscar de forma multiple, | es un or
res = exp.search("Python es un gran lenguaje de progrmación")
print(res.group())
res = exp.search("Pymysql es una herramienta para conectar Python con SQL")
print(res.group())
res = exp.search("Con Pycharm se pueden lograr grandes desarrollos")
print(res.group())
#%%
#? Character: a lo más una coincidencia (0 o 1 coincidencia)
expr = re.compile(r'Pyt(ho)?n')#va a buscar Pyth ó Python
match = expr.search("Python! a great language.")
print(match.group())
match = expr.search("Pytn! a great language.")
print(match.group())
match = expr.search("Pythohon a great language")#aparece 2 veces
print(match)#no tiene atributo group
#%%
#* Character: cero o más coincidencias
expr = re.compile(r"Pyt(ho)*n")#busca:Pytn,Python, Pythohon, Pythohohon,Pythohohon,...
match = expr.search("Welcome to the world of Pythohon")
print(match.group())
#%%
#+ Character: al menos una coincidencia
expr = re.compile(r'Pyth(o)+n')#Python, Pythooon,Pythoooooon,...
match = expr.search("Welcome to the world of Python")
print(match.group())
#%%
#{} : n coincidencias
regex = re.compile(r'(Ho){3}')#busca un numero especifico de coincidencias seguidas
match = regex.search("Santa dice HoHoHo")
print(match.group())
#%%
#{m,n} entre m y n coincidencias (pero máximo de coincidencias)
digit = re.compile(r'(\d){3,8}')#encuentre entre 3 y 8 numeros seguido, no más de ()
match = digit.search("123456789")
print(match.group())
#%%
#Match shortest possible string (add ? symbol) (mínimo de coincidencias)
digit = re.compile(r'(\d){4,8}?')#entre 4 y 8 numeros, solo devuelve 4, que son el minimo
match = digit.search('123456789')
print(match.group())
#%%
#Match the exact number of characters
string = 'The date is 22/10/2019'
lst = re.findall('[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}', string)
print(lst)
#%%
#Our own regular expression: Two vowel in a string
#construir nuestra propia expresion regular
regex = re.compile(r'[aeiouAEIOU]{2}')
string = "Welcome to the world of Ai"
print(regex.findall(string))
#%%
#Negative Character Class: ^
regex = re.compile(r'[^aeiouAEIOU]')#buscar todo lo que no son vocales
#los corchetes es desempacamiento
string = "The language is PythOn"
print(regex.findall(string))
#%%
#Case Insensitive
string = "The COSMOS is Infinite"
regex = re.compile(r'[aeiou]',re.I)#con re.I ignoro si son mayusculas o minisculas
print(regex.findall(string))
#%%
#Character Classes: \w, \d, \s
# \d: Any numeric digit[0–9]
# \w : sequence of word-like characters [a-zA-Z0–9_] that are not space
# \s: whitespace characters(space,newline,tab)

address = "568 Los Jardines 1145 Altos Dpto.501"
match = re.compile(r'\d+\s\w+\s\w+')
print(match.findall(address))