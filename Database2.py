import sqlite3

connection = sqlite3.connect("Bike.db")
#creation of the database
print(connection.total_changes)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Bikes (id INTEGER, location TEXT)")

cursor.execute("INSERT INTO bikes VALUES (1, '32 Eagle Lane')")
cursor.execute("INSERT INTO bikes VALUES (2, '12 Dixon Close')")
cursor.execute("INSERT INTO bikes VALUES (3, '25 Edward Fisher Drive')")

rows = cursor.execute("SELECT id, location FROM Bikes").fetchall()
print(rows)

from contextlib import closing

with closing(sqlite3.connect("Bikes.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)