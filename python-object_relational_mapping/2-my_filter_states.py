#!/usr/bin/python3
""" takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], state_name=argv[4], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE {state_name} ORDER BY id")
    rows = cur.fetchall()
    for i in rows:
        print(i)
        cur.close
        db.close