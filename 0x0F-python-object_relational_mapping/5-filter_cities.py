#!/usr/bin/python3
"""
A module to retrieve data from the cities and states table
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Access database to fetch data using the join statements
    """
    db = MySQLdb.connect(
            host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()
    query = """
    select cities.name from cities join states
    on cities.state_id = states.id where states.name LIKE BINARY %s
    order by cities.id asc
    """
    try:
        cursor.execute(query, (sys.argv[4],))
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        try:
            print(f"MySQL Error [e.args[0]]: {e.args[1]}")
        except IndexError:
            print(f"MySQL Error: {str(e)}")
    for i in range(len(rows)):
        print(f"{rows[i][0]}", end='')
        if (len(rows)-1 != i):
            print(', ', end='')
    print()
