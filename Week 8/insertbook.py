# This is to train with SQLlite3

import sqlite3
con = sqlite3.connect("lab2")
cur = con.cursor()

result = cur.execute("SELECT * FROM book")
print(result.fetchone())

sql = """
    INSERT into book VALUES 
        ('Harry Potter and the Philosophers Stone', 'J.K. Rowling', '123456'),
        ('Harry Potter and the Chamber of Secrets','J.K. Rowling', '473458')
"""

cur.execute(sql)
con.commit()

result = cur.execute("SELECT * FROM book")
print(result.fetchone())

con.close()