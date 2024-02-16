#!/usr/bin/python3
"""Script to get states starts with 'N' from database"""

import MySQLdb as db
from sys import argv as args

conn = db.connect(
    host="localhost", port=3306,
    user=args[1], passwd=args[2],
    db=args[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
