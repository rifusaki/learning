# ctrl + shtf + g

import sqlite3
import json

con = sqlite3.connect(r'C:\Users\rifuleva\Desktop\Offline\Estudio Offline\PythonUM\CM4\S4\roster_pollo.sqlite')
cur = con.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id      INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id      INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    title   TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

apath = input("Nombre de archivo:")
if len(apath) < 1:
    apath = r'C:\Users\rifuleva\Desktop\Offline\Estudio Offline\PythonUM\CM4\S4\roster_data.json'

'''
[
  [
    "Matthias",
    "si110",
    1
  ],
  [
    "Livia",
    "si110",
    0
  ],
  ...
  ]
'''

fl = open(apath).read()
js_d = json.loads(fl)

for entry in js_d:
    nombre = entry[0]
    curso = entry[1]
    rol = entry[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (nombre,))
    cur.execute('SELECT id FROM User WHERE name=?', (nombre,))
    id_usuario = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (curso,))
    cur.execute('SELECT id FROM Course WHERE title=?', (curso,))
    id_curso = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?,?,?)', (id_usuario, id_curso, rol))

con.commit()

'''
SELECT User.name,Course.title, Member.role FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
'''
