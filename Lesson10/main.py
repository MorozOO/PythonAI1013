import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
# cur.execute("CREATE TABLE first_table (name TEXT);")
# cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Oksana');")
connection.commit()
# cur.execute("SELECT rowid, name FROM first_table;")
cur.execute("SELECT rowid, name FROM first_table WHERE rowid=7;")
connection.commit()
res = cur.fetchall()
print(res)
# print(connection)
# print(cur)
connection.close()