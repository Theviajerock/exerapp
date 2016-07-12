import sqlite3

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

#create table users
cursor.execute("CREATE TABLE IF NOT EXISTS USERS(\
                USERNAME text,\
                PASSWORD text,\
                EMAIL text);")
conn.commit()
conn.close()

