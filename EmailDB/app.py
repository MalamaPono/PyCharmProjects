import sqlite3
import urllib
import re

connection = sqlite3.connect("emailDB.db")
cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("""
CREATE TABLE Counts (org TEXT, count INTEGER)""")

filename = input("Filename - ")
file = open(filename)

for line in file:
    if line.startswith("From: "):
        words = line.split()
        email_address = words[1]
        org = re.findall('@(.+)',email_address)
        org = org[0]

        cur.execute("SELECT count FROM Counts WHERE org = ?",(org,))
        row = cur.fetchone()
        if row == None:
            cur.execute("INSERT INTO Counts (org,count) VALUES (?,1)",(org,))
        else:
            cur.execute("UPDATE Counts SET count = count+1 WHERE org = ?",(org,))

connection.commit()

sqlstr = "SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()