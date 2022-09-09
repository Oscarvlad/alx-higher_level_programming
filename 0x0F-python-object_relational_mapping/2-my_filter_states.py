#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""


from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cur = db.cursor()
    request = "SELECT * FROM states WHERE BINARY name = '{}'".format(argv[4])
    cur.execute(request)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
