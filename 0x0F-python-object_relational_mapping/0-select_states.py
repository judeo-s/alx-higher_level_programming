#!/usr/bin/python3
"""
A module to select data from the states table
"""
import sys
import MySQLdb

db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], port=3306, passwd=sys.argv[2],
        db=sys.argv[3]
        )
cursor = db.cursor()
try:
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
except MySQLdb.Error as e:
    try:
        print(f"MySQL Error [e.args[0]]: {e.args[1]}")
    except IndexError:
        print(f"MySQL Error: {str(e)}")
for row in rows:
    print(row)
cursor.close()
db.close()
