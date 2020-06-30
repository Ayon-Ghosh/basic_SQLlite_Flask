import sqlite3
with sqlite3.connect('new.db') as connection:
	c = connection.cursor()
	c.execute ("UPDATE population SET population = 900000 WHERE city = 'New York'")
	print("\n New Data:\n")
	c.execute("SELECT * FROM population")
	rows = c.fetchall()
	for i in rows:
		print(i[0],i[1],i[2])