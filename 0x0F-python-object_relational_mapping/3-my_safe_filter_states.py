#!/usr/bin/python3
"""
    Script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!
"""


from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s;", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
