import sqlite3
from pypika import Query, Table, functions as fn

conn = sqlite3.connect('books.db')
cur = conn.cursor()

books = Table('books')
ratings = Table('ratings')

q = Query.from_(books).join(ratings).on(books.id == ratings.book_id).select(fn.Max(books.price).as_("max_price")).where(ratings.rating >= 3)
sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for i in rows:
    print(i)

conn.close()
