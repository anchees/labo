import sqlite3

conn = sqlite3.connect("constellations.db")
cursor = conn.cursor()
query = """
SELECT name, area
FROM constellations
ORDER BY area DESC
LIMIT 5;
"""
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
