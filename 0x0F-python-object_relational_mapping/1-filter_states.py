#!/usr/bin/python3
"""
A module to select data from the states table using the where clause
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Access database and retrieve specific data from the states table
    """
    db = MySQLdb.connect(
            host='localhost', user=sys.argv[1], passwd=sys.argv[2],
            port=3306, db=sys.argv[3]
            )
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM states WHERE id > 3")
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        try:
            print(f"MySQL Error [e.args[0]]: {e.args[1]}")
        except IndexError:
            print(f"MySQL Error: {str(e)}")
    for row in rows:
        print(row)
