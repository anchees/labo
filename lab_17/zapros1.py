import sqlite3
from pypika import Query, Table, functions as fn

conn = sqlite3.connect('warehouse.db')
cur = conn.cursor()

products = Table("products")
suppliers = Table("suppliers")

q = Query.from_(products).join(suppliers).on(products.supplier_id == suppliers.id).select(products.name, suppliers.name)
sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for i in rows:
    print(i)

conn.close()
