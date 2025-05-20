import sqlite3

conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()
query = """
SELECT Orders.OrderID, SUM(Books.Price * OrderItems.Quantity) AS Total
FROM Orders
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
JOIN Books ON OrderItems.BookID = Books.BookID
GROUP BY Orders.OrderID
"""
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()