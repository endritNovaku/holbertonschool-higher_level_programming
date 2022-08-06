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
    query = " ".join([
        "SELECT cities.name FROM cities",
        "INNER JOIN states",
        "ON states.id = cities.state_id",
        "WHERE states.name LIKE BINARY '{}' ORDER BY cities.id"
        ]).format(sys.argv[4])
    cur.execute(query)
    res = cur.fetchall()
    city = ", ".join([i[0] for i in res])
    print(city)
    cur.close()
    db.close()
