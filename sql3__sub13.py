import	sqlite3
with sqlite3.connect("car.db") as connection:				
    c =	connection.cursor()
    c.execute("DROP TABLE IF EXISTS inventory") 
    c.execute("DROP TABLE IF EXISTS inventory_New") 
    connection.commit()
    car = [('Ford', 'Focus', 100000),
           ('Ford', 'Focus', 200000),
           ('Ford', 'Focus', 300000),
           ('Honda','Civic', 450000),
           ('Honda', 'Civic', 34000),
           ('Honda', 'Civic', 230000),
           ('Ford', 'Ranger', 150000),
           ('Ford', 'Ranger', 180000),
           ('Ford', 'Ranger', 17500),
           ('Honda', 'Accord', 230000),
           ('Honda', 'Accord', 180050),
           ('Honda', 'Accord', 21500),
           ('Ford', 'Avenger', 450000),
           ('Ford', 'Avenger', 19000),
           ('Ford', 'Avenger', 123000),
             ]
    c.execute("CREATE TABLE IF NOT EXISTS Inventory(Car Text, Model Text, Quantity int)")
    c.executemany("INSERT INTO Inventory VALUES (?,?,?)", car)  
    connection.commit()       