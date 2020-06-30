import csv
import sqlite3
with sqlite3.connect('new.db') as connection:
	c = connection.cursor()
	employees = csv.reader(open("employees.csv"))
	c.execute("CREATE TABLE IF NOT EXISTS employees(firstname TEXT, lastname TEXT)")
	c.executemany("INSERT INTO employees(firstname,lastname) VALUES(?,?)", employees)
	connection.commit()