import sqlite3
from pypika import Query, Table, functions as fn

conn = sqlite3.connect('warehouse.db')
cur = conn.cursor()

products = Table("products")

q = Query.from_(products).groupby(products.supplier_id).select(products.supplier_id, fn.Avg(products.price))
sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for i in rows:
    print(i)

conn.close()