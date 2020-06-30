import	sqlite3
with sqlite3.connect("car.db") as connection:				
  c =	connection.cursor()
  orders = [('Ford', 'Focus', '2014-01-22'),
             ('Ford', 'Focus', '2014-01-23'),
             ('Ford', 'Focus', '2014-01-24'),
             ('Honda','Civic','2014-01-25'),
             ('Honda','Civic','2014-01-26'),
             ('Honda','Civic','2014-01-27'),
             ('Ford', 'Ranger','2014-01-28'),
             ('Ford', 'Ranger','2014-01-22'),
             ('Ford', 'Ranger','2014-01-23'),
             ('Honda','Accord','2014-01-24'),
             ('Honda','Accord','2014-01-25'),
             ('Honda','Accord','2014-01-26'),
             ('Ford', 'Avenger','2014-01-27'),
             ('Ford', 'Avenger','2014-01-28'),
             ('Ford', 'Avenger','2014-01-22'),
              ]
  c.execute("CREATE TABLE IF NOT EXISTS Car_Order(Car Text, Model Text, Order_Date Date)")         
  c.executemany("INSERT INTO Car_Order VALUES (?,?,?)", orders)  
  connection.commit()  