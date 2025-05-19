import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://en.wikipedia.org/wiki/IAU_designated_constellations"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"class": "wikitable sortable"})
if table is None:
    print("Таблица не найдена!")
    exit()
rows = table.find_all("tr")
print(f"Всего строк в таблице (с заголовком): {len(rows)}")

def parse_float(value):
    try:
        return float(value.replace(',', '.').replace('−', '-').strip())
    except:
        return None

def parse_int(value):
    try:
        return int(value.strip())
    except:
        return None

conn = sqlite3.connect("constellations.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE constellations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    genitive TEXT,
    abbreviation TEXT,
    family TEXT,
    area REAL,
    rank INTEGER,
    brightest_star TEXT,
    latitudes_visible TEXT
)
''')
conn.commit()

for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) < 8:
        continue

    name = cols[0].text.strip()
    genitive = cols[1].text.strip()
    abbreviation = cols[2].text.strip()
    family = cols[3].text.strip()
    area = parse_float(cols[4].text)
    rank = parse_int(cols[5].text)
    brightest_star = cols[6].text.strip()
    latitudes_visible = cols[7].text.strip()

    cursor.execute('''
        INSERT INTO constellations (name, genitive, abbreviation, family, area, rank, brightest_star, latitudes_visible)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, genitive, abbreviation, family, area, rank, brightest_star, latitudes_visible))

conn.commit()
conn.close()
