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

    query = "SELECT cities.name FROM cities JOIN states \
        ON cities.state_id = states.id WHERE states.name \
            LIKE BINARY %s ORDER BY cities.id ASC"

    cur.execute(query, (search_str + "%",))

    result = cur.fetchall()

    for i in range(len(result)):
        print(result[i][0], end=", " if i != len(result) - 1 else "\n")
