from typing import List

import pymysql
from config import *

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=name,
    cursorclass=pymysql.cursors.DictCursor
)
# Добавили данные в таблицу users
# with connection.cursor() as cur:
#     for i in range(len(surnames)):
#         cur.execute("INSERT INTO `users`(surname) VALUES(%s)", (surnames[i]))
#         connection.commit()
# Создание табли users
with connection.cursor() as cur:
    cur.execute("CREATE TABLE IF NOT EXISTS `users`("
                "`id` INT AUTO_INCREMENT,"
                "`surname` VARCHAR(20),"
                "`cash` INT DEFAULT 0,"
                "PRIMARY KEY(id)"
                ")")

# Показать таблицу
def show(table):
    with connection.cursor() as cur:
        cur.execute(f'SELECT * FROM {table}')
        for val in cur:
            print(val)
# Удалить таблицу
def del_table(table):
    with connection.cursor() as cur:
        cur.execute(f"DROP TABLE {table}")

def columns_table(table):
    with connection.cursor() as cur:
        cur.execute(f'SHOW COLUMNS FROM {table}')
        a = [len(i['Field']) for i in cur]
        cur.execute(f'SHOW COLUMNS FROM {table}')
        b = [len(i['Type']) for i in cur]

        # возьмём 2 первых индекса по ключам словаря...
        cur.execute(f'SHOW COLUMNS FROM {table}')
        key_ = [s for i in cur for s in i.keys()]
        key_ = key_[:2]

        # Посчитали общую длину
        cur.execute(f'SHOW COLUMNS FROM {table}')
        for s in cur:
            c = ','.join(list(('|', s[key_[0]], (' ' * (max(a) - len(s[key_[0]]))), '|', s[key_[1]],
                               (' ' * (max(b) - len(s[key_[1]]))), '|')))
        total_len = len(c)

        cur.execute(f'SHOW COLUMNS FROM {table}')
        print('-' * total_len)
        for i in cur:
            print('|', i[key_[0]], (' ' * (max(a) - len(i[key_[0]]))), '|', i[key_[1]],
                  (' ' * (max(b) - len(i[key_[1]]))), '|')
        print('-' * total_len)


def info():
    with connection.cursor() as cur:
        cur.execute("SHOW TABLES")
        val = [j for i in cur for j in i.values()]
        for i in val:
            print('Table:', i)
            columns_table(i)

def stroka(arg):
    b = [str(i) for i in arg]
    return b

def users():
    id_list = []
    surname_list = []
    cash_list = []
    with connection.cursor() as cur:
        cur.execute(f"SELECT * FROM users")
        lv = [stroka(i.values()) for i in cur]
        for i in lv: # Посчитали самое длинное слово
            id, surname, cash = i
            id_list.append(len(id))
            surname_list.append(len(surname))
            cash_list.append(len(cash))

        # Посчитали общую длину
        cur.execute(f'SHOW COLUMNS FROM users')
        for s in cur:
            c = ','.join(list(('|', id, (' ' * (max(id_list) - len(id))), '|',
                       surname, (' ' * (max(surname_list) - len(surname))), '|',
                       cash, (' ' * (max(cash_list) - len(cash))), '|')))
        total_len = len(c)

    # Keys
    with connection.cursor() as cur:
        cur.execute(f"SELECT * FROM users")
        print('+','-' * (total_len+1), '+', sep='')
        for i in cur:
            pass
        id, surname, cash = [s for s in i.keys()]
        print('|', id, (' ' * (max(id_list) - len(id))), '|',
              surname, (' ' * (max(surname_list) - len(surname))), '|',
              cash, (' ' * (max(cash_list) - len(cash))), '|')

    # Values
    with connection.cursor() as cur:
        cur.execute(f"SELECT * FROM users")
        lv = [stroka(i.values()) for i in cur]
        print('+','-' * (total_len+1), '+', sep='')
        for i in lv:
            id, surname, cash = i
            print('|', id, (' ' * (max(id_list) - len(id))), '|',
                       surname, (' ' * (max(surname_list) - len(surname))), '|',
                       cash, (' ' * (max(cash_list) - len(cash))), '   |')
        print('+','-' * (total_len+1), '+', sep='')

def garage():

