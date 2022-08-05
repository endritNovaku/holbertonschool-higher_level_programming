#!/usr/bin/python3
import MySQLdb
import sys

"""print states from the hbtn_0e_0_usa"""

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
