# 1. Создайте новую Базу данных
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное,
# то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)

# task 1
import sqlite3, random

conn = sqlite3.connect('bazadannyh_1.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user(id
INTEGER PRIMARY KEY AUTOINCREMENT, pol_1 INTEGER, pol_2 INTEGER)''')

a = random.randint(0,10)
b = random.randint(0,10)

cursor.execute('''INSERT INTO user(pol_1, pol_2) VALUES (?,?)''', (a, b))
conn.commit()
cursor.execute('''SELECT id FROM user''')
k = cursor.fetchall()
r = random.choice(k)
print(r)
cursor.execute('''SELECT pol_1,pol_2 FROM user WHERE id=(?)''',r)
for i in cursor:
    if i [0]%2 ==0 and i[1]%2 ==0:
        cursor.execute('''DELETE FROM user WHERE id=?''',r)
    elif i [0]%2 !=0 and i[1]%2 !=0:
        cursor.execute('''UPDATE user SET pol_1=2, pol_2=2, WHERE id=?''', r)
        # cursor.execute('''REPLACE INTO user (id, pol_1, pol-2) VALUES (?,2,2)''',r)       
conn.commit()
cursor.execute('''SELECT * FROM user''')
print(*cursor)



# cursor.execute('''DELETE FROM user WHERE id=9''')
# conn.commit()
#
# cursor.execute('''UPDATE user SET pol_1 = 2, pol_2 = 2 WHERE rowid = 2''')
# cursor.execute('''SELECT * FROM user''')
# for i in cursor:
#     print(i)
