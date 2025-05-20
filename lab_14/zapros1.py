import sqlite3

conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()
query = """
SELECT Books.Title, Books.Price, Authors.FirstName, Authors.LastName
FROM Books
JOIN Authors ON Books.AuthorID = Authors.AuthorID
"""
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()