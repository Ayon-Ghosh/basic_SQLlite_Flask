import sqlite3
import random
with sqlite3.connect("newnum.db") as connection:				
   c =	connection.cursor()
   c.execute("CREATE TABLE IF NOT EXISTS numbers(num int)")
   listA = []
   for i in range(100):
      c.execute("INSERT INTO numbers VALUES(?)", (random.randint(1,100),))
   connection.commit()

   