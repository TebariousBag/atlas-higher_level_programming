#!/usr/bin/python3
""" takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id",
                (argv[4],))
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close
    db.close
