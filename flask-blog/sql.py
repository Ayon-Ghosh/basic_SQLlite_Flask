import sqlite3
with sqlite3.connect("blog.db") as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS posts(Title Text, Post Text)")
	c.execute("INSERT INTO posts VALUES('Good', 'I am Good')")
	c.execute("INSERT INTO posts VALUES('Well', 'I am Well')")
	c.execute("INSERT INTO posts VALUES('Excellent', 'I am Excellent')")
	c.execute("INSERT INTO posts VALUES('Okay', 'I am Okay')")
