#!/usr/bin/python3
''' Script that takes in an argument\
    and displays all values in the states\
    table of hbtn_0e_0_usa where name matches the argument
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE name LIKE BINARY '{}'\
                   ORDER BY id ASC".format(argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
