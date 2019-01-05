import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="invoker",         # your username
                     passwd="invoker",  # your password
                     db="parse",
                     port=5432)

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM twogis")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0])

db.close()