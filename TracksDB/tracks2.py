import xml.etree.ElementTree as ET
import sqlite3

connection = sqlite3.connect("Databases/TracksDataModel2.db")
cur = connection.cursor()

cur.executescript("""

DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
    
CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name Text UNIQUE
);

CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    genre Text UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title Text UNIQUE,
    artist_id INTEGER
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    genre_id INTEGER,
    album_id INTEGER,
    len INTEGER,
    count INTEGER,
    rating INTEGER
);

""")

def lookup(dic,key):
    found = False
    for child in dic:
        if found == True:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

file = open("Library.xml")

tree = ET.parse(file)
tracks = tree.findall("dict/dict/dict")

for track in tracks:
    if (lookup(track,"Track ID") == None):
        continue

    name = lookup(track,'Name')
    artist = lookup(track,'Artist')
    album = lookup(track,'Album')
    genre = lookup(track,'Genre')
    count = lookup(track,'Play Count')
    rating = lookup(track,'Rating')
    length = lookup(track,'Total Time')

    if name == None or artist == None or album == None or genre == None:
        continue

    print(name,artist,album,genre,count,rating,length)

    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist,))
    cur.execute("SELECT id FROM Artist WHERE name=?",(artist,))
    artist_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Genre (genre) VALUES (?)",(genre,))
    cur.execute("SELECT id FROM Genre WHERE genre=?", (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Album (title,artist_id) VALUES (?,?)",(album,artist_id))
    cur.execute("SELECT id FROM Album WHERE title=?",(album,))
    album_id = cur.fetchone()[0]

    cur.execute("""INSERT OR REPLACE INTO Track (title,genre_id,album_id,len,count,rating) 
            VALUES (?,?,?,?,?,?)""",(name,genre_id,album_id,length,count,rating))

    connection.commit()

cur.close()