#!/usr/bin/python3
"""print states from the hbtn_0e_0_usa"""
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
    query = " ".join(["SELECT cities.id cities.name, states.name",
                      "FROM cities INNER JOIN states ON cities.state_id=states.id",
                      "ORDER BY cities.id"])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
