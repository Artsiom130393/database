# 3. Заполнить таблицу БД названиями песен с указанием их длительности
# (то есть колонка с названием и колонка со временем в секундах)
# Из этой таблицы собрать все записи, с длительностью больше 60 секунд и
# записать их в текстовый файл (название и время).


import sqlite3
conn = sqlite3.connect('songs.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS 
tracks(id INTEGER PRIMARY KEY AUTOINCREMENT, trek_1 TEXT, seconds_1 INTEGER )''')

a = ['The Bangles-Walk Like An Egyptian', 'ABBA-Waterloo', 'Akcent-Kylie',
             'Ирина Аллегрова-Привет,Андрей']
b = [40, 80, 90, 50]

for i,j in zip(a,b):
    cursor.execute('''INSERT INTO tracks(trek_1,seconds_1) VALUES (?,?)''', (i,j))
conn.commit()
cursor.execute('''SELECT * FROM tracks''')
for i in cursor:
    print(i)

with open('new_file.txt', 'w') as f:
    for i in cursor:
        print(i)
        if i[1]>60: f.write(str(i)+'\n')



