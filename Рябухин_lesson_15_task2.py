# 2. Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
#  my_list = [‘Home’, ‘Work’, 29, 9, 2022]
# Если элемент списка слово, записать его в соответствующую таблицу,
# затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел,
# если нечётное, то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello»

# Task 2
import sqlite3

conn = sqlite3.connect('user_1.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tabl_1(id
INTEGER PRIMARY KEY AUTOINCREMENT, pol_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tabl_2(id
INTEGER PRIMARY KEY AUTOINCREMENT, pol_2 INTEGER )''')
conn.commit()
cursor.execute('''SELECT * FROM tabl_1''')
cursor.execute('''SELECT * FROM tabl_2''')


my_list = ['Home', 'Work', 29, 9, 2022]
a = 0

print(my_list)
for i in my_list:
    if type(i) is str:
        cursor.execute('''INSERT INTO tabl_1(pol_1) VALUES (?)''', [i])
        conn.commit()
    elif i % 2:
        cursor.execute('''INSERT INTO tabl_2 (pol_2) VALUES ('нечётное')''')
        conn.commit()
    # if type(i) == str:
    #     cursor.execute('''INSERT INTO tabl_1(pol_1) VALUES (?)''', (i,))
    #     conn.commit()
    #     cursor.execute('''INSERT INTO tabl_2 (pol_2) VALUES (?)'''(len(i,),))
    #     conn.commit()
    # elif type(i) == int:
    #     if i%2:
    #         cursor.execute('''INSERT INTO tabl_1 (pol_1) VALUES (?)'''(len(i,), ))
    #     else:
    #         cursor.execute('''INSERT INTO tabl_1 (pol_1) VALUES ('нечётное')''')
cursor.execute('''SELECT * FROM tabl_1''')
print(*cursor)
cursor.execute('''SELECT * FROM tabl_1''')
cursor.execute('''SELECT * FROM tabl_2''')
print(*cursor)
