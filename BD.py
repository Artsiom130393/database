import sqlite3


conn = sqlite3.connect('my_data_base.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tablica(id INTEGER PRIMARY KEY AUTOINCREMENT, 
kolonka_1 TEXT, kolonka_2 TEXT)''')

# cursor.execute('''INSERT INTO tablica(kolonka_1, kolonka_2) VALUES ('Artem', 'Irina') ''')
# conn.commit()

d = 'Artem'
f = 'Irina'
cursor.execute('''INSERT INTO tablica(kolonka_1, kolonka_2) VALUES (?,?) ''', (d,f))
conn.commit()
cursor.execute('''SELECT * FROM tablica''')
# print(*cursor)
# print(cursor.fetchall())


cursor.execute('''SELECT * FROM tablica WHERE kolonka_1 = 'Artem' ''')
print(*cursor)


