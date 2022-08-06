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
    query = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE states.name=%s ORDER BY cities.id"
    state = sys.argv[4]
    cur = db.cursor()
    cur.execute(query, (state, ))
    rows = cur.fetchall()
    city = ""
    for row in rows:
        city = city + row[0]
        city = city + ', '
    for i in range(len(city) - 2):
        print(city[i], end='')
    print()
