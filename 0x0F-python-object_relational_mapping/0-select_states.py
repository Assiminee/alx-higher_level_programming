#!/usr/bin/python3
"""states models
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    host = "localhost"
    port = 3306
    user = sys.argv[1]  # user trying to connect to the database
    pwd = sys.argv[2]   # user password
    db = sys.argv[3]    # database name

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
