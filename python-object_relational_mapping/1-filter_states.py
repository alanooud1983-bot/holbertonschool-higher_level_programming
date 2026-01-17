#!/usr/bin/python3
"""
Lists all states starting with N (uppercase) from the database hbtn_0e_0_usa
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    query = """
    SELECT *
    FROM states
    WHERE BINARY name LIKE 'N%'
    ORDER BY id ASC
    """

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
