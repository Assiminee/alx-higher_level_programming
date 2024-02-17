#!/usr/bin/python3
"""Fetching data from database where name starts with N
sorted in ascending order of id
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

    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
    cursor = con.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    con.close()
