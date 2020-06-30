import sqlite3
with sqlite3.connect('car.db') as connection:
	c = connection.cursor()
car = [
	('Ford',	'Fusion',	500000),
	('Honda',	'CrossFire',	200000),
	('Ford',	'Impala',	2500000),
	('Honda',	'Zit',	1250000),	
	('Ford',	'Explorer',	350000)
 ]

c.executemany("INSERT INTO inventory VALUES(?,?,?)", car)
connection.commit()

#c.execute("CREATE TABLE IF NOT EXISTS inventory_new(car_make TEXT, model TEXT, number INT) ") 
#c.execute("DROP TABLE inventory_new")
#c.execute("CREATE TABLE IF NOT EXISTS inventory_New(car_make TEXT, model TEXT, Quantity INT) ") 
#c.execute("INSERT INTO inventory_New(car_make TEXT, model TEXT, Quantity INT) SELECT Name,Species, IQ FROM inventory")
connection.commit()



