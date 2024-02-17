#!/usr/bin/python3
"""states models
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

    cursor = con.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    con.close()
