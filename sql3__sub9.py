import sqlite3
with sqlite3.connect('car.db') as connection:
	c = connection.cursor()
	c.execute("SELECT * FROM inventory WHERE Name = 'Ford'")
	row = c.fetchall()
	for i in row:
		print(i[0],i[1],i[2])