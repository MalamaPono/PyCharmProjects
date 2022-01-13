import sqlite3
import csv

filename = input("Enter a file - ")
file = open(filename)
reader = csv.reader(file)

connection = sqlite3.connect("tech.db")
cur = connection.cursor()

cur.executescript("""

DROP TABLE IF EXISTS Stocks;

CREATE TABLE Stocks(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Date TEXT,
    Apple REAL,
    Google REAL,
    Msft REAL
);

""")

for row in reader:
    date = row[1]
    apple = row[2]
    google = row[3]
    msft = row[4]

    try:
        apple = float(apple)
        google = float(google)
        msft = float(msft)
    except:
        continue

    # if you want to insert into a table, you need to insert everything in
    # one command, or else it moves to the next row and does the next insert
    cur.execute("INSERT INTO Stocks (Date,Apple,Google,Msft) VALUES (?,?,?,?)", (date,apple,google,msft))

    connection.commit()

cur.close()