#!/usr/bin/python3
import MySQLdb
import sys

user, pwd, db = sys.argv[1:4]

con = MySQLdb.connect(host='localhost', port=3306,
                      user=user, passwd=pwd, db=db)

cursor = con.cursor()
cursor.execute('SELECT * FROM states')
rows = cursor.fetchall()

for row in rows:
    print(row)
