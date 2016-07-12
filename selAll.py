import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()
for row in cur.execute("SELECT * FROM USERS;"):
    print(row)
conn.commit()
conn.close()
