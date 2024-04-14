#!/usr/bin/python3
"""
A module to select data fro the states table using the where clause
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Access database and retrieve specific data from the states and cities
    table
    """
    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
        )
    cursor = db.cursor()
    query = """select cities.id, cities.name, states.name from cities join
    states on cities.state_id = states.id order by cities.id"""
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        try:
            print(f"MySQL Error [e.args[0]]: {e.args[1]}")
        except IndexError:
            print(f"MySQL Error: {str(e)}")
    for row in rows:
        print(row)
