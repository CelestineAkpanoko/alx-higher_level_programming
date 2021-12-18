#!/usr/bin/python3
'''Lists all states with a name starting with N
'''
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        db_conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cur = db_conn.cursor()
        cur.execute(
                'SELECT * FROM states WHERE name IS NOT NULL AND LIKE "N%" ' + 
                'ORDER BY states.id ASC;'
                )
        results = cur.fetchall()
        for result in results:
            print(result)
        db_conn.close()
