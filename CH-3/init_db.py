import sqlite3
import os
import sys

from sqlalchemy.engine import cursor

conn = sqlite3.connect("Sales/sales.db")

cursor = conn.cursor()

cursor.execute