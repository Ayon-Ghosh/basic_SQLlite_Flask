import sqlite3
import random
with sqlite3.connect("newnum.db") as connection:				
   c =	connection.cursor()
   c.execute("CREATE TABLE IF NOT EXISTS numbers_1(num_1 int)")
   listA = []
   for i in range(100):
   	  listA.append(random.randint(1,100))
   c.executemany("INSERT INTO numbers_1 VALUES(?)", listA)
   connection.commit()