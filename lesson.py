# # 4. Создайте класс на тему животных.
# # Используйте статические и динамические переменные,
# # дочерний (1 или более) классов на конкретное животное.
# # Публичные и приватные методы. Полиморфизм (одинаковые названия методов info в обоих классах,
# # которые выводят информацию о животных, либо о конкретном животном данного класса).
# # Создайте объекты каждого класса и обратитесь к каждому методу. Напишите один staticmethod,
# # один classmethod, к которым также обратитесь.
#
# class Animals:
#     kol_male = 44
#     kol_female = 30
#     __vid = 'predators'
#     f = 2
#     def __init__(self, name, poroda):
#         self.name = name
#         self.poroda=poroda
#
#
#     def __private_method(self):
#         print('Class method called')
#
#     def insideclass(self):
#         print("Private variable:", Animals.__vid)
#
#     def info(self):
#         print(f'Male: {self.kol_male}, Female: {self.kol_female}')
#
#     @staticmethod
#     def get_class_details():
#         print('This is class Animals')
#
# class Cats(Animals):
#     kol_male = 5
#     kol_female = 12
#     def __init__(self,name,clor,vid):
#         super().__init__(name, vid)
#         self.color=clor
#
#     def info(self):
#         print(f'Male: {self.kol_male}, Female: {self.kol_female}')
#
#     @staticmethod
#     def get_class_details():
#         print(Cats.kol_female)
#
#     @classmethod
#     def classmethod(cls):
#         print('Cats have 4 paws')
#         # cls.info(self=cat)
#         print(cls)
# class Dogs(Animals):
#     kol_male = 6
#     kol_female = 8
#     def __init__(self, name, prd):
#         super().__init__(name, prd)
#
#     def info(self):
#         print(f'Male: {self.kol_male}, Female: {self.kol_female}')
#
#     def form_para(self):
#         if self.kol_female<self.kol_male:print(f'We have {self.kol_female} couple of dogs')
#         else:print(f'We have {self.kol_male} couple of dogs')
#
# cat=Cats('Murka','grey','British')
# cat.classmethod()
# birds=Animals('Ptashka','Tit')
# Animals.get_class_details()
# dog=Dogs('Pesik','Labrador')
# print(cat.color)
# print(cat.poroda)
# print(birds.poroda)
# cat.info()
# birds.info()
# dog.info()
# birds.insideclass()
# Animals.get_class_details()
# Cats.get_class_details()
# Cats.classmethod()
# dog.form_para()



#Базы данных (DB) на языке SQL
# БД - это совокупность данных, которые связаны между собой и организованы
#Виды БД:
    #1. Иерархическая БД - такая база данных может быть представлена в виде дерева,
    # которое состоит из объектов разных уровней
    #2. Сетевая БД - обобщение иерархической БД,
    # только элементы вышестоящего уровня ммогут быть связаны с элементами низких уровней
    #3. Реляционная БД - такая БД состоит из таблиц, связанных друг с другом

#SQLite (SQL - structured query language - язык структурированных запросов) import sqlite3.
# SQLite работает с реляционными БД
# ОСновные типы данных в SQL: INTEGER, TEXT, REAL
#SQL - язык запросов для управления системой управления базы данных (СУБД)
#SQLite - одна из СУБД, которая работает на языке SQL

# import sqlite3

#Создаем базу данных
# conn = sqlite3.connect('my_data_base.db') #создат (или не создаст, если уже есть)БД с таким названием и привяжет к переменной conn
# #создаем объект cursor (указатель), который поможет взаимодействовать с БД
# cursor = conn.cursor()
# #Создаем таблицу с двумя колонками типа TEXT
# cursor.execute('''CREATE TABLE IF NOT EXISTS tablica(id INTEGER PRIMARY KEY AUTOINCREMENT, kolonka_1 TEXT, kolonka_2 TEXT)   ''')
#execute - это метод для всех взаимодействий с таблицами БД

#Заполнение таблицы БД
# cursor.execute('''INSERT INTO tablica(kolonka_1, kolonka_2) VALUES ('Artem','Irina')''')
#INSERT INTO вносит данные в таблицу, VALUES показывает, какие именно данные внести
# conn.commit() #сохраняет изменения. Нужно обязательно сохранять при каждом изменение таблицы, но не при создании
# d = 'Ahmed'
# f = 'Irina'
# cursor.execute('''INSERT INTO tablica(kolonka_1, kolonka_2) VALUES (?,?)''',(d,f))
#с помощью знаков ? можно указать значения не в коде SQL, а после него (после кавычек)
# Значения указываются в виде кортежа
# conn.commit()
# cursor.execute('''SELECT * FROM tablica''') #SELECT * FROM выбрать все записи из таблицы

# print(cursor.fetchall()) #fetchall вытаскивает всё содержимое указателя cursor
# print(*cursor) #*cursor это тоже самое, что fetchall
# print(cursor.fetchone()) #fetchone покажет только первую запись

# cursor.execute('''SELECT * FROM tablica WHERE kolonka_1 = 'Artem' ''') #WHERE уточняет, что нужно выбрать в SELECT
# cursor.execute('''SELECT * FROM tablica ORDER BY kolonka_1 ''') #ORDER BY покажет, как сортировать записи
# cursor.execute('''SELECT * FROM tablica WHERE kolonka_1 LIKE 'A%' ''') # WHERE LIKE покажет записи, начинающиеся на A
# cursor.execute('''SELECT * FROM tablica WHERE kolonka_1 LIKE '%m' ''') #покажет записи, заканчивающиеся на m
# cursor.execute('''SELECT * FROM tablica WHERE kolonka_1 LIKE '%tem%' ''')#внутри есть tem
#
# print(*cursor)

#Task_1. Создайте новую Базу данных.
# В ней создайте таблицу с тремя полями, два текстовых, одно – целое число.
# Число запрашивается с клавиатуры, а слова задаются статически.
# * Выведите каждую запись в отдельную строку

# import sqlite3
# conn = sqlite3.connect('my_data_base.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id
# INTEGER PRIMARY KEY AUTOINCREMENT, kolonka_1 TEXT, kolonka_2 TEXT, kolonka_3 INTEGER)''')
# a,b = 'Hello','World'
# c = int(input('Введите целое число: '))
# cursor.execute('''INSERT INTO tab_1(kolonka_1, kolonka_2, kolonka_3) VALUES (?,?,?)''',(a,b,c))
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# for i in cursor:
#     print(i)

#Удаление записей из таблицы
# cursor.execute('''DELETE FROM tab_1 WHERE id=1''') #DELETE удаляет запись, которую мы уточнили в WHERE
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# for i in cursor:
#     print(i)
# cursor.execute('''DELETE FROM tab_1''') #DELETE удаляет все записи таблицы
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# for i in cursor:
#     print(i)

#Task_2
# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без учёта id
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД
#
# import sqlite3, random
# conn = sqlite3.connect('my_data_base.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS lid_1
# (id INTEGER PRIMARY KEY AUTOINCREMENT, kolonka_1 INTEGER, kolonka_2 INTEGER)''')
# a = random.randint(0,10)
# b = random.randint(0,10)
# cursor.execute('''INSERT INTO lid_1(kolonka_1, kolonka_2) VALUES (?,?)''',(a,b))
# conn.commit()
# cursor.execute('''SELECT kolonka_1, kolonka_2 FROM lid_1''')
# summ = 0
# count = 0
# for i in cursor:
#     summ += sum(i)
#     count += 1
#     print(i)
# print(summ/(count*2))
# print(count)
# if (summ/count) > count:
#     cursor.execute('''DELETE FROM lid_1 WHERE id=4''')
#     conn.commit()
# cursor.execute('''SELECT * FROM lid_1''')
# for i in cursor:
#     print(i)



#ДЗ на вторник:
# 1. Создайте новую Базу данных
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное,
# то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)
#
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
#
# 3. Заполнить таблицу БД названиями песен с указанием их длительности
# (то есть колонка с названием и колонка со временем в секундах)
# Из этой таблицы собрать все записи, с длительностью больше 60 секунд и записать их в текстовый файл (название и время).