import sqlite3

conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()
query = """
SELECT Orders.OrderID, Orders.OrderDate, Books.Title, OrderItems.Quantity
FROM Orders
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
JOIN Books ON OrderItems.BookID = Books.BookID
"""
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()