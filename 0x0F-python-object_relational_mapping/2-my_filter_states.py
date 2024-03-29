#!/usr/bin/python3
"""select the state that is in the arguments"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")
    cur = db.cursor()
    s = " ".join(["SELECT * FROM states",
                  "WHERE name LIKE BINARY '{}'",
                  "ORDER BY id ASC"]).format(sys.argv[4])
    cur.execute(s)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
