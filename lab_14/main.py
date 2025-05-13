import sqlite3

conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Authors;
""")

cursor.executescript("""
CREATE TABLE Authors (
    AuthorID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Biography TEXT
);

CREATE TABLE Books (
    BookID INTEGER PRIMARY KEY,
    Title TEXT,
    Price REAL,
    AuthorID INTEGER,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    OrderDate TEXT,
    Status TEXT
);

CREATE TABLE OrderItems (
    OrderItemID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    BookID INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);
""")

cursor.executescript("""
INSERT INTO Authors VALUES
(1, 'Лев', 'Толстой', 'Русский писатель, автор "Войны и мира"'),
(2, 'Фёдор', 'Достоевский', 'Русский философ и писатель'),
(3, 'Александр', 'Пушкин', 'Основоположник современной русской литературы');

INSERT INTO Books VALUES
(1, 'Война и мир', 799.00, 1),
(2, 'Анна Каренина', 650.00, 1),
(3, 'Преступление и наказание', 720.00, 2),
(4, 'Идиот', 680.00, 2),
(5, 'Евгений Онегин', 550.00, 3);

INSERT INTO Orders VALUES
(1, '2025-05-01', 'Доставлен'),
(2, '2025-05-03', 'В обработке');

INSERT INTO OrderItems VALUES
(1, 1, 1, 2),
(2, 1, 3, 1),
(3, 2, 2, 1),
(4, 2, 5, 3);
""")

conn.commit()

cursor = conn.cursor()

print("\n1. Все книги с именами авторов:")
for row in cursor.execute("""
SELECT Books.Title, Books.Price, Authors.FirstName, Authors.LastName
FROM Books
JOIN Authors ON Books.AuthorID = Authors.AuthorID
"""):
    print(row)

print("\n2. Заказы и книги в них:")
for row in cursor.execute("""
SELECT Orders.OrderID, Orders.OrderDate, Books.Title, OrderItems.Quantity
FROM Orders
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
JOIN Books ON OrderItems.BookID = Books.BookID
"""):
    print(row)

print("\n3. Сумма каждого заказа:")
for row in cursor.execute("""
SELECT Orders.OrderID, SUM(Books.Price * OrderItems.Quantity) AS Total
FROM Orders
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
JOIN Books ON OrderItems.BookID = Books.BookID
GROUP BY Orders.OrderID
"""):
    print(row)
conn.close()
