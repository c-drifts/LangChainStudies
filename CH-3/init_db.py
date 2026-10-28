import sqlite3
import os
import sys

from sqlalchemy.engine import cursor

os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

conn = sqlite3.connect("Sales/sales.db")

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    total REAL
); """)

cursor.execute(""" insert into Orders values 
    (1, 'John Doe', 'Laptop', 1, 1000, 1000), 
    (2, 'Jane Smith', 'Mouse', 2, 25, 50); 
    """)
    
conn.commit()
conn.close()