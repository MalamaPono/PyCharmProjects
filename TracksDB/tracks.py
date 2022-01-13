import xml.etree.ElementTree as ET
import sqlite3

connection = sqlite3.connect("Databases/TracksDataModel.db")
cur = connection.cursor()

# For this example, the data model is not as rich as the one created in practice during the lecture
# videos because there is no genres for the tracks as it is not provided by apple's xml data.
cur.executescript("""
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Album(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
    );

    CREATE TABLE Track(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        len INTEGER, 
        count INTEGER,
        rating INTEGER
    );

""")

file = open("Library.xml")

def lookup(dic,key):
    found = False
    for child in dic:
       if found:
           return child.text
       if child.tag == 'key' and child.text == key:
           found = True
    return None


tree = ET.parse(file)
tracks = tree.findall("dict/dict/dict")

for track in tracks:
    if (lookup(track,"Track ID") == None):
        continue

    name = lookup(track,'Name')
    artist = lookup(track,'Artist')
    album = lookup(track,'Album')
    count = lookup(track,'Play Count')
    rating = lookup(track,'Rating')
    length = lookup(track,'Total Time')

    if name == None or artist == None or album == None:
        continue

    print(name,artist,album,count,rating,length)

    # add to the database

    cur.execute("INSERT OR IGNORE INTO ARTIST (name) VALUES (?)",(artist,))
    cur.execute("SELECT id FROM Artist WHERE name = ?",(artist,))
    artist_id = cur.fetchone()[0]

    # Insert or ignore means that if that thing we are inserting is already there, don't insert it instead of throwing a
    # traceback because as specified earlier in the table, some things like Artist name or Album title must be unique.

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, len, rating, count) 
            VALUES ( ?, ?, ?, ?, ? )''',
                (name, album_id, length, rating, count))

    connection.commit()
cur.close()

