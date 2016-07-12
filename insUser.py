from sys import argv
import sqlite3

username = argv[1]
password = argv[2]
email = argv[3]

if len(argv) == 4:
    conn = sqlite3.connect("db.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO USERS VALUES(?,?,?);", [username, password, email])
    conn.commit()
    conn.close()
else:
    print(len(argv))
    print("Please enter the script, then the username, then the password")


