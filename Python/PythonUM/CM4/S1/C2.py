# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:46:46 2021

@author: rifuleva
"""

import sqlite3

nom = input('Base de datos SQLite - ')
if len(nom) < 1:
    dbn = r'C:\Users\rifuleva\Desktop\Offline\Estudio Offline\PythonUM\CM4\C2.sqlite' # raw string
con = sqlite3.connect(dbn)
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Cnts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

nom = input('Nombre de archivo - ')
if len(nom) < 1:
    nom = r'C:\Users\rifuleva\Desktop\Offline\Estudio Offline\PythonUM\CM4\mbox.txt' # raw string
fhan = open(nom)


for line in fhan:
    if not line.startswith('From '):
        continue
    line.rstrip()
    dom = line.split()[1].split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (dom,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (dom,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (dom,))

con.commit()
print('\n') 

prnt = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for a in cur.execute(prnt):
    print(a[0], a[1])