import sqlite3
inventory_values  = (
        ("Honda", "Accord", 122),
        ("Toyota","Camry", 100),
        ("Nissan","Altima", 30)
        )
with sqlite3.connect("car.db") as connection:
            c = connection.cursor()
            c.execute("CREATE TABLE inventory(Name TEXT, Species TEXT, IQ int)")
            c.executemany("INSERT INTO inventory VALUES(?,?,?)", inventory_values)
            connection.commit()
            connection.close()
            c.close()