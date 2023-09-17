#!/usr/bin/python3

"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset='utf8'
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `cur` \
                INNER JOIN `states` as `st` \
                ON `cur`.`state_id` = `st`.`id` \
                ORDER BY `cur`.`id`")
    print(", ".join([i[2] for i in cur.fetchall() if i[4] == argv[4]]))
    cur.close()
    db.close()
