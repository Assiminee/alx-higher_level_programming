#!/usr/bin/python3
"""Fetching all cities and the states they are in
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    host = "localhost"
    port = 3306
    user, pwd, db = sys.argv[1:4]

    con = MySQLdb.connect(
            host=host, port=port, user=user, passwd=pwd, db=db
    )

    query = "SELECT c.id, c.name, s.name\
             FROM cities c INNER JOIN states s\
             ON c.state_id = s.id\
             ORDER BY c.id ASC;"

    cursor = con.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    con.close()
