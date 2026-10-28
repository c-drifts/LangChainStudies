import sqlite3

conn = sqlite3.connect("Sales/sales.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Orders")
rows = cursor.fetchall()

for row in rows:
    print(row)