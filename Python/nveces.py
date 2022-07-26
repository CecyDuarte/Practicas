# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 11:13:25 2021

@author: almac
"""

#repetir n cantidad de veces con función tee
from itertools import tee
numeros=[1,2,3,4,5]
print(numeros)

print()
cantidad=input("introduce la cantidad de veces a repetir: ")
cantidad=int(cantidad)

resultado=tee(numeros,cantidad)

for r in resultado:
    print(list(r))