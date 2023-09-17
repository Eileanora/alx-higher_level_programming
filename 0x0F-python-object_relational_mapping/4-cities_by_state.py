#!/usr/bin/python3
'''script that lists all cities from the database hbtn_0e_4_usa'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    INNER JOIN states\
                    ON cities.state_id = states.id\
                    ORDER BY cities.id ASC")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()
