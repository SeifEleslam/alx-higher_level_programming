#!/usr/bin/python3
"""Script to get all states from database"""

import MySQLdb as db
from sys import argv as args

if __name__ == '__main__':
    conn = db.connect(
        host="localhost", port=3306,
        user=args[1], passwd=args[2],
        db=args[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
