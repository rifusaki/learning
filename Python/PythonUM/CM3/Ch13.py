# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:00:15 2021

@author: rifuleva
"""

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors WINK
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ejercicio
url = input('URL - ')
if len(url.rstrip()) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1006169.xml'
print('Recuperando...', url)
pagby = urlopen(url, context=ctx).read()

arbol = ET.fromstring(pagby)
num_com = arbol.findall('.//count') # Investigar XPath: https://www.w3schools.com/xml/xpath_syntax.asp
print('Cantidad:', len(num_com))
sumlst = [ int(x.text) for x in num_com]
print('Suma:', sum(sumlst))