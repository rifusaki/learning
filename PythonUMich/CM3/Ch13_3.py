# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:34:35 2021

@author: rifuleva
"""

import urllib.parse
import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

servicio = input('URL de servicio: ')
if len(servicio) < 1:
    servicio = 'http://py4e-data.dr-chuck.net/json?'
direccion = input('Dirección: ')
if len(direccion) < 1:
    direccion = 'Virginia Commonwealth University'

urldef = servicio + urllib.parse.urlencode({'address' : direccion, 'key' : 42})
print('Recuperando...', urldef)

datos = urllib.request.urlopen(urldef).read().decode()
arbol = json.loads(datos)
print('Place ID:', arbol['results'][0]['place_id'])
