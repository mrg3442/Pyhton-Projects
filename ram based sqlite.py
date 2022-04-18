import sqlite3

conn = sqlite3.connect(':memory:')


tblInfo = (('Jean-Baptise Zorg', 'Human', 122),
           ('Korben Dallas', 'Meat Popsicle', 100),
           ("Ak'not", 'Mangalore', -5))

with conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS roster")
    c.execute("CREATE TABLE roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO roster VALUES(?, ?, ?)", tblInfo)
    c.execute("SELECT name, IQ FROM roster WHERE Species == 'Human'")
    for row in c.fetchall():
        print(row)
