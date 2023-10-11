# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:19:50 2021

@author: rifuleva
"""

from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = input('Escribe la URL: ')
if len(url1) < 1:
    url1 = 'http://py4e-data.dr-chuck.net/comments_1006170.json'
print('Recuperando...', url1)

datos = urlopen(url1).read().decode()
print(len(datos), 'caracteres recuperados.')

arbol = json.loads(datos)
counts = [a['count'] for a in arbol['comments']]
print('Cantidad:', len(counts))
print('Suma;', sum(counts))