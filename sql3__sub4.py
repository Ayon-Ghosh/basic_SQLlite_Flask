import sqlite3
with sqlite3.connect('new.db') as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS population (city TEXT, state TEXT, population INT)")
	connection.commit()
	c.close()
with sqlite3.connect('new.db') as connection:
	c = connection.cursor()
	c.execute("INSERT INTO population VALUES('New York','NY', 84000000)")
	c.execute("INSERT INTO population VALUES('San Fran','NY', 84000000)")	
	connection.commit()
	

