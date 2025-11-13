# This is to train with SQLlite3

import sqlite3
con = sqlite3.connect("lab2")
cur = con.cursor()

cur.execute("CREATE TABLE book(title, author, ISBN)")
print("Table has been created")

con.close()