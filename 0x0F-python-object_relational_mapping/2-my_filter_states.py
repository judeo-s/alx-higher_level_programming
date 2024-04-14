#!/usr/bin/python3
"""
A module to select data fro the states table using the where clause
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    Access database and retrieve specific data from the states table
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
