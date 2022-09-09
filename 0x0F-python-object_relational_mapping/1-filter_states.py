#!/usr/bin/python3
"""
   script that lists all states with a name starting with
   N (upper N) from the database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
        WHERE name LIKE BINARY 'N%' ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
