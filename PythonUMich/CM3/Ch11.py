# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:56:52 2021

@author: rifuleva
"""

import re
import numpy as np

busqueda = input('Expresión regular para buscar: ')
archivo = input('Archivo: ')

try:
    fhan = open(archivo, 'r')
except:
    print('Haga eso bien')
    exit()

# Ejercicio 1    

clin = 0
for line in fhan:
    linea = line.rstrip()
    if re.search(busqueda, linea):
        clin += 1
    
print('\n {0} tiene {1} línea(s) que coinciden con "{2}"'.format(archivo, clin, busqueda))

# Ejercicio 2
nvrec = []
for line in fhan:
    linea = line.rstrip()
    temp = re.findall("^New Revision: ([0-9]+)", linea)
    nvrec.extend(temp)

revl = []
for i in nvrec:
    revl.append(int(i))

print("Promedio rev:", np.mean(revl))

# Ejercicio 3 - Chuck
exefh = open("regex_sum_1006165.txt")

sumex = 0
for line in exefh:
    temn = re.findall('[0-9]+', line)
    sumex += sum([int(x) for x in temn])

print("Total:", sumex)