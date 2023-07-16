import sqlite3
conn = sqlite3.connect('filename.db')
cur = conn.cursor()
cur.execute('SQL statement')
conn.commit()
conn.close()