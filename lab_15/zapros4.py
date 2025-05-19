import sqlite3

conn = sqlite3.connect("constellations.db")
cursor = conn.cursor()
query = """
SELECT rank, GROUP_CONCAT(name, ', ') AS constellations
FROM constellations
GROUP BY rank
ORDER BY rank;
"""
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()