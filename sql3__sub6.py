import sqlite3
with sqlite3.connect('new.db') as connection:
   c = connection.cursor()
   c.execute("SELECT firstname,lastname FROM employees")
   rows = c.fetchall()
   for i in rows:
	    print(i[0],i[1])


#for row in c.execute("SELECT firstname, lastname from employees"):
#	print(row)