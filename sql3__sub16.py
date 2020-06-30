import	sqlite3
with sqlite3.connect("car.db") as connection:				
	c =	connection.cursor()
	c.execute("SELECT * FROM Inventory")
	rows = c.fetchall()
	for i in rows:
		print(i[0],i[1],'\n', i[2])
		c.execute("SELECT COUNT(Order_Date) from Car_Order where Model = ?",(i[1])
		order_count=c.fetchone()
		print(order_count)