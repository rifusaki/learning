import sys

import driver

if 'sqlite3' not in sys.modules:    import sqlite3
if 'requests' not in sys.modules:   import requests
if 'ssl' not in sys.modules:    import ssl
if 'BeautifulSoup' not in sys.modules:  from bs4 import BeautifulSoup
if 'urlparse' not in sys.modules:    from urllib.parse import urlparse
if 'pandas' not in sys.modules: import pandas as pd

# Setup DB
con = sqlite3.connect('input.sqlite')
cur = con.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Principal;
DROP TABLE IF EXISTS Productos;
DROP TABLE IF EXISTS Tiendas
''')

cur.executescript('''
CREATE TABLE IF NOT EXISTS Principal (
    url TEXT UNIQUE,
    producto INTEGER,
    tienda INTEGER,
    precio TEXT,
    PRIMARY KEY (url),
    FOREIGN KEY (producto) REFERENCES Productos(nombre),
    FOREIGN KEY (tienda) REFERENCES Tiendas(nombre)
);

CREATE TABLE IF NOT EXISTS Productos (
    id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Tiendas (
    id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE
)
''')

# File + ids
arch = input('Archivo de datos: ')
if len(arch) < 1:
    arch = 'data.xlsx'

while True:
    try:
        prod = pd.read_excel(arch, sheet_name=0, header=None).to_dict(orient='split')
        inf_p = pd.read_excel(arch, sheet_name=1, header=None).to_dict(orient='split')
        break
    except:
        print('Intenta de nuevo')

inf = {}
for i in inf_p['data']:
    inf[i[0]] = [i[1]]

# Get pages
cabezas = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
for entry in prod['data']:
    print('Recuperando...',entry[1])

    fulldom = urlparse(entry[1]).netloc.split('.')[1]
    id_pre = inf[fulldom][0]

    pag = requests.get(entry[1], headers=cabezas)
    try:
        sopa = BeautifulSoup(pag.text, 'html.parser')
    except:
        sopa = BeautifulSoup(pag.content, 'html.parser')

    if fulldom == 'backcountry':
        precio = sopa.find({'class':'chakra-text css-17wknbl'})['value'].strip()
    else:
        try:
            precio = sopa.find(id=id_pre)['value'].strip()
        except:
            precio = sopa.find(id=id_pre).get_text().strip()

    print(entry[0], precio)

    cur.execute('INSERT OR IGNORE INTO Productos (nombre) VALUES (?)', (entry[0],))
    cur.execute('SELECT id FROM Productos WHERE nombre=?', (entry[0],))
    id_producto = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Tiendas (nombre) VALUES (?)', (fulldom,))
    cur.execute('SELECT id FROM Tiendas WHERE nombre=?', (fulldom,))
    id_tienda = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Principal (url,producto,tienda,precio) VALUES (?,?,?,?)', (entry[1],id_producto,id_tienda,precio))

    con.commit()


#backcountry chakra-text css-17wknbl
#
#
print('TADÁ, FINAL')
