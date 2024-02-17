#!/usr/bin/python3
"""Fetching all cities and the states they are in
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    host = "localhost"
    port = 3306
    user, pwd, db = sys.argv[1:4]
    safeInput = (sys.argv[4],)  # User input to use in a prepared statement

    con = MySQLdb.connect(
            host=host, port=port, user=user, passwd=pwd, db=db
    )

    query = "SELECT name FROM cities WHERE state_id = \
             (SELECT id FROM states WHERE name LIKE BINARY %s)\
             ORDER BY cities.id ASC;"

    cursor = con.cursor()
    cursor.execute(query, safeInput)
    rows = cursor.fetchall()

    for row in rows:
        delim = ", " if row is not rows[len(rows) - 1] else "\n"
        for col in row:
            print(col, end="")
        print(end=delim)

    cursor.close()
    con.close()
