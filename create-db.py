import sqlite3

conn = sqlite3.connect('collection.db')

conn.execute("CREATE TABLE users(email VARCHAR(25), password VARCHAR(25))")

conn.execute("INSERT INTO users VALUES('a@b.com', 'password1')")
conn.execute("INSERT INTO users VALUES('b@c.com', 'password2')")

conn.commit()

conn.close()
