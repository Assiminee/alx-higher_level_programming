#!/usr/bin/python3
"""Fetching data from database where name matches user input
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    host = "localhost"
    port = 3306
    user, pwd, db = sys.argv[1:4]
    searchTerm = sys.argv[4]

    con = MySQLdb.connect(
            host=host, port=port, user=user, passwd=pwd, db=db
    )

    query = "SELECT * FROM states\
            WHERE name LIKE BINARY '{}'\
            ORDER BY id ASC;".format(searchTerm)

    cursor = con.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    con.close()
