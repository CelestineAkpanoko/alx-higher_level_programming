#!/usr/bin/python3
'''Lists all states with a name starting with N
'''
import sys
import MySQLdb

if sys.argv >= 4:
    db_conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db_conn.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC;')
    states = cur.fetchall()
    for state in states:
        print(state)
    db_conn.close()
