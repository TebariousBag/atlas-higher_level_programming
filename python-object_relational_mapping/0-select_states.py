#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "--main__":
	db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
	cur = db.cursor()
	cur.execute("SELECT * FROM states ORDER BY id")
	rows = cur.fetchall()
	for row in rows:
		for col in row:
			print(row)
	# Close all cursors
	cur.close()
	# Close all databases
	db.close()
