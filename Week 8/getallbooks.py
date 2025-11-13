# This is to train with SQLlite3

import sqlite3
con = sqlite3.connect("lab2")
cur = con.cursor()

for row in cur.execute("SELECT * FROM book"):
    print(f"row{row}")
