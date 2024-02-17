#!/usr/bin/python3
"""Script to get states starts with 'N' from database"""

import MySQLdb as db
from sys import argv as args

if __name__ == '__main__':
    conn = db.connect(
        host="localhost", port=3306,
        user=args[1], passwd=args[2],
        db=args[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities\
             LEFT JOIN states ON states.id = cities.state_id\
             WHERE states.name = %s\
          ORDER BY cities.id ASC", (args[4],))
    query_rows = cur.fetchall()
    first = True
    for row in query_rows:
        if not first:
            print(', ', end='')
        print(row[0], end='')
        first = False
    print()
    cur.close()
    conn.close()
