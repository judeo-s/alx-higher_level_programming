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
    db = MySQLdb.connect(
            host='localhost', user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)

    cursor = db.cursor()
    query = f"SELECT * FROM states \
            WHERE name LIKE BINARY '{sys.argv[4]}' \
            ORDER BY states.id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
