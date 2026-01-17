#!/usr/bin/python3
"""
Safe from SQL injection:
Lists states where name matches the argument (exact match).
Usage: ./3-my_safe_filter_states.py <user> <password> <database> <state name>
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # Parameterized query (SAFE)
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (state,)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
