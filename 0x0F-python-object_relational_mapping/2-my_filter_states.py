#!/usr/bin/python3
'''Displays values of states where name matches the argument taken
'''
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.arg)v >= 5:
        db_conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cur = db_conn.cursor()
        state_name = sys.argv[4]
        cur.execute('SELECT * FROM states WHERE name="{}"' + 
               ' ORDER BY id ASC;'.format(state_name))
        results = cur.fetchall()
        for result in results:
            print(result)
        db_conn.close()

