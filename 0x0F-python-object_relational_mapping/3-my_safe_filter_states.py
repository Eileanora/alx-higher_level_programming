#!/usr/bin/python3
''' Same as last task but the script should\
    be safe against MySQL injections!
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY %s\
                    ORDER BY id ASC", (argv[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
