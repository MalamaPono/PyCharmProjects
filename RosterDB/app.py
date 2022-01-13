import json
import sqlite3

connection = sqlite3.connect('RosterDataModel.db')
cur = connection.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

file = open("roster_data_sample.json")
str_data = file.read()
json_data = json.loads(str_data)

for entry in json_data:
    user = entry[0]
    course = entry[1]
    role = entry[2]

    print(user,course,role)

    cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)",(user,))
    cur.execute("SELECT id FROM User WHERE name=?",(user,))
    user_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (course,))
    cur.execute("SELECT id FROM Course WHERE title=?", (course,))
    course_id = cur.fetchone()[0]

    cur.execute("INSERT OR REPLACE INTO Member (user_id,course_id,role) VALUES (?,?,?)",(user_id,course_id,role))

    connection.commit()

cur.close()
