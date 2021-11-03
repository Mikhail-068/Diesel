import pymysql
from config import *

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=name,
    cursorclass=pymysql.cursors.DictCursor
)

# Показать таблицу
def show(table):
    with connection.cursor() as cur:
        cur.execute(f'SELECT * FROM {table}')
        for val in cur:
            print(val)

def info(table):
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
            c = ','.join(list(('|', s[key_[0]], (' ' * (max(a) - len(s[key_[0]]))), '|', s[key_[1]], (' ' * (max(b) - len(s[key_[1]]))), '|')))
        total_len = len(c)

        cur.execute(f'SHOW COLUMNS FROM {table}')
        print('-' * total_len)
        for i in cur:
            print('|', i[key_[0]], (' ' * (max(a) - len(i[key_[0]]))), '|', i[key_[1]], (' ' * (max(b) - len(i[key_[1]]))), '|')
        print('-' * total_len)



