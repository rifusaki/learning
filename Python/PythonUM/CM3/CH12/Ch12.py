# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:56:32 2021

@author: rifuleva
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# EJ1C
url = input('Ingresar - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1006167.html'
pagina_bytes = urlopen(url, context=ctx).read()
pagina_bs = BeautifulSoup(pagina_bytes, 'html.parser')

listll = []
for i in pagina_bs('span'):
    listll.extend(i.contents)

listf = [int(x) for x in listll]
print('Suma: ', sum(listf))

# EJ2C
url = input('Ingresar - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Coll.html'

try:
    pos = int(input('Posición - '))
    cnt = int(input('Iteraciones - '))
except:
    print('ajá')
    exit()

print('')
loopcount = 0
while loopcount <= cnt:
    print('Escaneando...', url)
    pagina_bytes = urlopen(url, context=ctx).read()
    pagina_bs = BeautifulSoup(pagina_bytes, 'html.parser')    
    url = str(pagina_bs('a')[pos-1].get('href', None))
    loopcount += 1