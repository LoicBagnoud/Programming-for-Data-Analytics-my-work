# This is to train with SQLlite3

import sqlite3
con = sqlite3.connect("lab2")
cur = con.cursor()

book = {}
book["title"] = input("Please enter book title: ")
book["author"] = input("Please enter book author: ")
book["ISBN"] = input("Please enter book ISBN: ")

data = [book]
#data = [{"title":"Frankenstein", "author":"Mary Shelley","ISBN":"587433"}]

sql = "INSERT INTO book VALUES (:title, :author, :ISBN)"
cur.executemany(sql,data)
con.commit()

for row in cur.execute("SELECT * FROM book"):
    print(f"row{row}")