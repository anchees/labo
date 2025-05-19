import sqlite3

conn = sqlite3.connect("constellations.db")
cursor = conn.cursor()
query = """
SELECT f.name AS family_name, COUNT(c.id) AS count
FROM constellations c
LEFT JOIN families f ON c.family_id = f.id
GROUP BY f.name
ORDER BY count DESC;
"""
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()