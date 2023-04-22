#!/usr/bin/python3
"""
A module that connects to a mysql database and selects
all states where name matches the 4th cmd arg
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_str = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name)

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = '%s' ORDER BY id ASC" % search_str)

    result = cur.fetchall()

    for row in result:
        print(row)
