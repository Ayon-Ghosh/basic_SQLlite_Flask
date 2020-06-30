import	sqlite3
with sqlite3.connect("car.db") as connection:				
	c =	connection.cursor()
	sql = {'Focus count':"SELECT SUM(Quantity) FROM Inventory WHERE Model =='Focus'",
	       'Civic count':"SELECT SUM(Quantity) FROM Inventory WHERE Model =='Civic'",
	       'Ranger count':"SELECT SUM(Quantity) FROM Inventory WHERE Model =='Ranger'",
	       'Accord count':"SELECT SUM(Quantity) FROM Inventory WHERE Model =='Accord'",
	       'Accord count':"SELECT SUM(Quantity) FROM Inventory WHERE Model =='Accord'"
	}

	for keys, values in sql.items():
		c.execute(values)
		result = c.fetchone()
		print(keys+":",+result[0])