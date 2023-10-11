# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 06:43:41 2021

@author: rifuleva
"""

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect(r'C:\Users\rifuleva\Desktop\Offline\Estudio Offline\PythonUM\CM4\S2\S2.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

arbol = ET.parse(r'C:\Users\rifuleva\Desktop\Offline\Estudio Offline\PythonUM\CM4\S2\Library.xml')

todo = arbol.findall("dict/dict/dict")
print("Cantidad: ", len(todo))

def buscar(estructura, key):
    pres = False
    for child in estructura:
        if pres == True:
            return child.text
        if child.tag == "key" and child.text == key:
            pres = True
    return None

for item in todo:
    if buscar(item, "Track ID") == None:
        continue
    name = buscar(item, 'Name')
    artist = buscar(item, 'Artist')
    album = buscar(item, 'Album')
    genre = buscar(item, 'Genre')
    count = buscar(item, 'Play Count')
    rating = buscar(item, 'Rating')
    length = buscar(item, 'Total Time')
    
    print(name, artist, album, genre, count, rating, length)
    
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist, ))
    cur.execute('''SELECT id FROM Artist WHERE name = ?''', (artist, ))
    try:
        artist_id = cur.fetchone()[0]
    except Exception:
        artist_id = None
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre, ))
    cur.execute('''SELECT id FROM Genre WHERE name = ?''', (genre, ))
    try:
        genre_id = cur.fetchone()[0]    
    except Exception:
        genre_id = None
    
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)''', (album, artist_id))
    cur.execute('''SELECT id FROM Album WHERE title = ?''', (album, ))
    try:
        album_id = cur.fetchone()[0]
    except Exception:
        album_id = None
    
    cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count)
                VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))
    
conn.commit()

cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')
for row in cur:
     print(row)

conn.close()