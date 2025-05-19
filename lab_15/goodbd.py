import sqlite3

conn = sqlite3.connect("constellations.db")
cursor = conn.cursor()

cursor.execute("SELECT DISTINCT family FROM constellations")
families = cursor.fetchall()

cursor.execute("DROP TABLE IF EXISTS families")
cursor.execute("""
CREATE TABLE families (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

for fam in families:
    cursor.execute("INSERT INTO families (name) VALUES (?)", (fam[0],))

cursor.execute("ALTER TABLE constellations RENAME TO old_constellations")

cursor.execute("""
CREATE TABLE constellations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    genitive TEXT,
    abbreviation TEXT,
    area REAL,
    rank INTEGER,
    brightest_star TEXT,
    latitudes_visible TEXT,
    family_id INTEGER,
    FOREIGN KEY (family_id) REFERENCES families(id)
)
""")
cursor.execute("""
SELECT o.name, o.genitive, o.abbreviation, o.area, o.rank, o.brightest_star, o.latitudes_visible, f.id
FROM old_constellations o
JOIN families f ON o.family = f.name
""")

for row in cursor.fetchall():
    cursor.execute("""
        INSERT INTO constellations (name, genitive, abbreviation, area, rank, brightest_star, latitudes_visible, family_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, row)

cursor.execute("DROP TABLE old_constellations")

cursor.execute("DROP TABLE IF EXISTS stars")
cursor.execute("""
CREATE TABLE stars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

cursor.execute("SELECT DISTINCT brightest_star FROM constellations WHERE brightest_star != ''")
stars = cursor.fetchall()
for star in stars:
    cursor.execute("INSERT OR IGNORE INTO stars (name) VALUES (?)", (star[0],))

cursor.execute("ALTER TABLE constellations RENAME TO tmp_constellations")
cursor.execute("""
CREATE TABLE constellations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    genitive TEXT,
    abbreviation TEXT,
    area REAL,
    rank INTEGER,
    latitudes_visible TEXT,
    family_id INTEGER,
    star_id INTEGER,
    FOREIGN KEY (family_id) REFERENCES families(id),
    FOREIGN KEY (star_id) REFERENCES stars(id)
)
""")

cursor.execute("""
SELECT tmp.name, tmp.genitive, tmp.abbreviation, tmp.area, tmp.rank, tmp.latitudes_visible, tmp.family_id, s.id
FROM tmp_constellations tmp
LEFT JOIN stars s ON tmp.brightest_star = s.name
""")

for row in cursor.fetchall():
    cursor.execute("""
        INSERT INTO constellations (name, genitive, abbreviation, area, rank, latitudes_visible, family_id, star_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, row)

cursor.execute("DROP TABLE tmp_constellations")
conn.commit()
conn.close()
