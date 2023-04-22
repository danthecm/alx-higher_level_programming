#!/usr/bin/python3
"""
A module that connects to a mysql database and selects
all states in the state table
"""
import sys
import MySQLdb


username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

db = MySQLdb.connect(host="localhost", user=username,
                     passwd=password, db=db_name)

cur = db.cursor()

cur.execute("SELECT * FROM states")

result = cur.fetchall()

for row in result:
    print(row)
