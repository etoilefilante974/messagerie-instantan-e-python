import sqlite3

connection = sqlite3.connect("C:/Users/jauze/Desktop/dbz.db")

cursor=connection.cursor()

bn=cursor.execute('SELECT * FROM t_nb')


print(bn.fetchall())

