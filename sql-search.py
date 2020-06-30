import sqlite3
import random
with sqlite3.connect("newnum.db") as connection:
  c = connection.cursor()
  prompt = "Select the operation that you want to perform [1-5]: 1.Average 2.Max 3.Min 4.Sum 5.Exit"
  user_int_map = {'1':"SELECT AVG(num) FROM numbers",
                  '2':"SELECT MAX(num) FROM numbers",
                  '3':"SELECT MIN(num) FROM numbers",
                  '4':"SELECT COUNT(num) FROM numbers",
                  }
  while True:
  	user_inp = input(prompt)
  	if user_inp in user_int_map.keys():
  	 	  c.execute(user_int_map[user_inp])
  	 	  result = c.fetchone()
  	 	  print(result)
    elif user_inp==5:
  	    print('Exit')
        break