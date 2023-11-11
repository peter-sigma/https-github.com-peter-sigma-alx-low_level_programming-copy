#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument but safe from MySQL injections!
"""

import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
        )

        cursor = db.cursor()
        query = "SELECT id, name \
        FROM states \
        WHERE name LIKE BINARY '{}' ORDER BY id ASC;".format(argv[4])
        cursor.execute(query)
        for result in cursor:
            print(result)
        cursor.close()
    except Exception:
        pass
