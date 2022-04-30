import pymysql
from config import host, user, password, name
import sqlite3

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=name,
    cursorclass=pymysql.cursors.DictCursor
)
connection2 = sqlite3.connect('business.db')

#         with connection.cursor() as cur:
#             cur.execute("SELECT * FROM garage")

# with connection.cursor() as cur:
#     cur.execute("SELECT * FROM reset")
#     sum_ = 0
#     for i in cur:
#         # print(i['LitresReset'])
#         sum_ += i['LitresReset']
#
#     print(sum_)

class diesel_base():
    def del_table(self, table):
        with connection.cursor() as cur:
            cur.execute(f"DROP TABLE {table}")
    def columns_table(self, table):
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
    def show_tables(self):
        with connection.cursor() as cur:
            cur.execute("SHOW TABLES")
            val = [j for i in cur for j in i.values()]
            for i in val:
                print('Table:', i)
                self.columns_table(i)
    def users(self):
        id_list = []
        surname_list = []
        cash_list = []
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM users")
            lv = [[str(i) for i in(i.values())] for i in cur]
            for i in lv:  # Посчитали самое длинное слово
                id, surname, cash = i
                id_list.append(len(id))
                surname_list.append(len(surname))
                cash_list.append(len(cash))

            # Посчитали общую длину
            cur.execute('SHOW COLUMNS FROM users')
            for s in cur:
                c = ','.join(list(('|', id, (' ' * (max(id_list) - len(id))), '|',
                                   surname, (' ' * (max(surname_list) - len(surname))), '|',
                                   cash, (' ' * (max(cash_list) - len(cash))), '|')))
            total_len = len(c)

        # Keys
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM users")
            print('=' * 10, 'U S E R S', '=' * 11)
            print('+', '-' * (total_len + 1), '+', sep='')
            for i in cur:
                pass
            id, surname, cash = [s for s in i.keys()]
            print('|', id, (' ' * (max(id_list) - len(id))), '|',
                  surname, (' ' * (max(surname_list) - len(surname))), '|',
                  cash, ' ' * 2, '|')

        # Values
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM users")
            lv = [[str(i) for i in(i.values())] for i in cur]
            print('+', '-' * (total_len + 1), '+', sep='')
            for i in lv:
                id, surname, cash = i
                print('|', id, (' ' * (max(id_list) - len(id))), '|',
                      surname, (' ' * (max(surname_list) - len(surname))), '|',
                      cash, (' ' * (max(cash_list) - len(cash))), '   |')
            print('+', '-' * (total_len + 1), '+', sep='')
    def garage(self):
        id_list = []
        date_list = []
        liters_list = []
        id_driver_list = []
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM garage")
            lv = [[str(i) for i in(i.values())] for i in cur]
            for i in lv:  # Посчитали самое длинное слово
                id2, date_, liters, id_driver = i
                id_list.append(len(id2))
                date_list.append(len(date_))
                liters_list.append(len(liters))
                id_driver_list.append(len(id_driver))

            # Посчитали общую длину
            surnames = 'Титов,Алексеев,Савельев,Черкасов,Юрьев,Сажнев,Авилочкин,Дильдин,Усачев,Кизиль,Бирюков,Жирнов,' \
                       'Пустынников,Назин'.split(',')

            cur.execute("SELECT DISTINCT id_driver FROM garage")
            list_val = []
            for i in cur:
                list_val.append(len(surnames[list(i.values())[0]-1]))
            cur.execute('SHOW COLUMNS FROM garage')
            for s in cur:
                c = ','.join(list(('|', id2, (' ' * (max(id_list) - len(id2))), '|',
                                   date_, (' ' * (max(date_list) - len(date_))), '|',
                                   liters, (' ' * ((max(liters_list) - len(liters))+3)), '|',
                                   surnames[int(id_driver) - 1], (' ' * (max(list_val) - len(surnames[int(id_driver) - 1]))))))



            total_len = len(c)

        # # Keys

        len_surnames = [len(i) for i in surnames]
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM garage")
            print('=' , 'G A R A G E', '=' )
            print('+', '-' * (total_len), '+', sep='')
            for i in cur:
                pass
            id1, date_, liters, id_driver = [s for s in i.keys()]
            print('|', id1, '',   '|',
                  date_, (' ' * (max(date_list) - len(date_))), '|',
                  liters, '|',
                  id_driver,  '|')

        # Values
        with connection.cursor() as cur:
            cur.execute("SELECT DISTINCT id_driver FROM garage")
            list_val = []
            for i in cur:
                list_val.append(len(surnames[list(i.values())[0]-1]))

        with connection.cursor() as cur:
            cur.execute("SELECT * FROM garage")
            lv = [[str(i) for i in(i.values())] for i in cur]
            print('+', '-' * (total_len), '+', sep='')
            for i in lv:
                id2, date_, liters, id_driver = i
                print('|', id2, (' ' * (max(id_list) - len(id2))), '|',
                      date_, (' ' * (max(date_list) - len(date_))), '|',
                      liters, (' ' * ((max(liters_list) - len(liters)) + 3)), '|',
                      surnames[int(id_driver) - 1], (' ' * (max(list_val) - len(surnames[int(id_driver) - 1]))), '|')
            print('+', '-' * (total_len), '+', sep='')
    def add_users(self):
        print('=== USERS ===')
        s = input('Surname: ').capitalize()
        surnames = 'Титов,Алексеев,Савельев,Черкасов,Юрьев,Сажнев,Авилочкин,Дильдин,Усачев,Кизиль,Бирюков,Жирнов,' \
                   'Пустынников,Назин'.split(',')
        id_surnames = [i + 1 for i in range(len(surnames)) if s in surnames[i]]
        money = input('Cash: ')

        with connection.cursor() as cur:
            cur.execute(f"UPDATE users SET cash = {money} WHERE id = {id_surnames[0]}")
            connection.commit()
    def add_garage(self):

        print('=== GARAGE ===')
        date_ = input('Date: ')
        s = input('Surname: ').capitalize()
        surnames = 'Титов,Алексеев,Савельев,Черкасов,Юрьев,Сажнев,Авилочкин,Дильдин,Усачев,Кизиль,Бирюков,Жирнов,' \
                   'Пустынников,Назин'.split(',')
        id_surnames = [i + 1 for i in range(len(surnames)) if s in surnames[i]]
        id_ = id_surnames[0]
        liters = int(input('Liters: '))

        # Добавляем в MySQL
        with connection.cursor() as cur:
            cur.execute(f"INSERT INTO garage (date_, liters, id_driver) VALUES"
                        f"('{date_}', {liters}, {id_})")
            connection.commit()

        # Добавляем в SQLite
        cur2 = connection2.cursor()
        surname = s

        cur2.execute('SELECT id FROM garage')
        for i in cur2:
            pass
        id_ = (int(i[0]) + 1)

        for i, v in enumerate(surnames):
            if surname in v:
                id_driver = i+1

        cur2.execute(f"INSERT INTO garage(id, Дата, Фамилия, Литры, id_driver)"
                     f" VALUES ({id_}, '{date_}', '{surname}', {liters}, {id_driver})")

        connection2.commit()
        connection2.close()

    def add_reset(self):
        dateReset = input('Дата сброса: ')
        litrReset = int(input('Сколько литров ДТ сдали: '))
        Name = input('Введите имя кому сдали ДТ: ')
        with connection.cursor() as cur:
            cur.execute('INSERT INTO reset(DateReset, LitresReset, Name)' \
                        ' VALUES (%s, %s, %s)', (dateReset, litrReset, Name))
            connection.commit()


    def condition(self):
        dt1, dt2 = input('Введите дату c ... по ...:').split(',')

        id_list = []
        date_list = []
        liters_list = []
        id_driver_list = []
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM garage")
            lv = [[str(i) for i in(i.values())] for i in cur]
            for i in lv:  # Посчитали самое длинное слово
                id, date_, liters, id_driver = i
                id_list.append(len(id))
                date_list.append(len(date_))
                liters_list.append(len(liters))
                id_driver_list.append(len(id_driver))

            # Посчитали общую длину
            cur.execute('SHOW COLUMNS FROM garage')
            for s in cur:
                c = ','.join(list(('|', id, (' ' * (max(id_list) - len(id))), '|',
                                   date_, (' ' * (max(date_list) - len(date_))), '|',
                                   liters, (' ' * (max(liters_list) - len(liters))), '|',
                                   id_driver, (' ' * (max(id_driver_list) - len(id_driver))), '|')))
            total_len = len(c)

        # # Keys
        with connection.cursor() as cur:
            cur.execute("SELECT date_ as 'Дата', liters as 'Литры', id_driver as 'Фамилия' FROM garage")
            print('=' * 10, 'ВЫБОРКА ПО ДАТЕ', '=' * 10)
            print('+', '-' * (total_len + 4), '+', sep='')
            for i in cur:
                pass
            date_, liters, id_driver = [s for s in i.keys()]
            print('|', date_, (' ' * (max(date_list) - len(date_))), '|',
                  liters, (' ' * 1), '|',
                  id_driver, ' ' * 4, '|')
        #
        # # Values
        surnames = 'Титов,Алексеев,Савельев,Черкасов,Юрьев,Сажнев,Авилочкин,Дильдин,Усачев,Кизиль,Бирюков,Жирнов,' \
                   'Пустынников,Назин'.split(',')
        len_surnames = [len(i) for i in surnames]
        data2 = f'SELECT id_driver as "Фамилия",' \
                f'SUM(liters) as "Сумма", COUNT(liters) as "Кол-во раз" FROM `garage`' \
                f'WHERE garage.date_ >= "{dt1}" AND garage.date_ <= "{dt2}"' \
                f'GROUP BY id_driver'
        with connection.cursor() as cur:
            cur.execute(data2)
        lv = [[str(i) for i in(i.values())] for i in cur]
        print('+', '-' * (total_len + 4), '+', sep='')
        for i in lv:
            id_driver, Summa2, Count2 = i

            cc = len(','.join(
                ('|', surnames[int(id_driver) - 1], (' ' * ((max(len_surnames) - len(surnames[int(id_driver) - 1])))), '|',
                 Summa2, (' ' * (len("Cумма") - len(Summa2) - 1)), '|',
                 Count2, (' ' * (len("Кол-во раз") - len(Count2) - 1)), '|')))

        data1 = f'SELECT date_, liters, id_driver FROM `garage`' \
                f'WHERE garage.date_ >= "{dt1}" AND garage.date_ <= "{dt2}"'
        with connection.cursor() as cur:
            cur.execute(data1)
            lv = [[str(i) for i in(i.values())] for i in cur]
            print('+', '-' * (total_len + 4), '+', sep='')
            for i in lv:
                date_, liters, id_driver = i

                print('|', date_, (' ' * (max(date_list) - len(date_))), '|',
                      liters, (' ' * ((max(liters_list) - len(liters)) + 3)), '|',
                      surnames[int(id_driver) - 1], (' ' * ((max(len_surnames) - len(surnames[int(id_driver) - 1])))), '|')
            print('+', '-' * (total_len + 4), '+', sep='')
            print()
            cur.execute(data2)
        # Длина
        id_driver_list = []
        sum_list = []
        count_list = []
        with connection.cursor() as cur:
            cur.execute(data2)
            lv = [[str(i) for i in(i.values())] for i in cur]
            for i in lv:  # Посчитали самое длинное слово
                id_driver, sum_, count_ = i
                id_driver_list.append(len(id_driver))
                sum_list.append(len(sum_))
                count_list.append(len(count_))

            # Посчитали общую длину
            cur.execute(data2)
            for s in cur:
                c = ','.join(list(('|', id_driver, (' ' * (max(id_driver_list) - len(id_driver))), '|',
                                   sum_, (' ' * (max(sum_list) - len(sum_))), '|',
                                   count_, (' ' * (max(count_list) - len(count_))), '|')))
            total_len = len(c)

            # Keys
            print('=' * 15, 'Итого', '=' * 15)
            print('+', '-' * (cc - 2), '+', sep='')
            with connection.cursor() as cur:
                cur.execute(data2)
                for i in cur:
                    pass
                id_driver, Summa, Count = [s for s in i.keys()]
                print('|', id_driver, (' ' * (max(len_surnames) - len(id_driver))), '|',
                      Summa, '|',
                      Count, '|')

        # Values
        surnames = 'Титов,Алексеев,Савельев,Черкасов,Юрьев,Сажнев,Авилочкин,Дильдин,Усачев,Кизиль,Бирюков,Жирнов,' \
                   'Пустынников,Назин'.split(',')
        len_surnames = [len(i) for i in surnames]

        with connection.cursor() as cur:
            cur.execute(data2)
            lv = [[str(i) for i in(i.values())] for i in cur]
            print('+', '-' * (cc - 2), '+', sep='')
            for i in lv:
                id_driver, Summa2, Count2 = i

                print('|', surnames[int(id_driver) - 1], (' ' * ((max(len_surnames) - len(surnames[int(id_driver) - 1])))),
                      '|',
                      Summa2, (' ' * (len("Cумма") - len(Summa2) - 1)), '|',
                      Count2, (' ' * (len("Кол-во раз") - len(Count2) - 1)), '|')

            print('+', '-' * (cc - 2), '+', sep='')

    def reset(self):
        with connection.cursor() as cur:
            cur.execute('SELECT * FROM reset')
            print('= R E S E T =')
            print('-' * (len('DateReset  | LitresReset | Name')+2))
            for i in cur:
                pass
            id_key, date_key, litr_key, name_key =i.keys()
            print(date_key, ' |', litr_key, '|', name_key)
            print('-' * (len('DateReset  | LitresReset | Name')+2))

        with connection.cursor() as cur:
            cur.execute('SELECT * FROM reset')
            # for i in cur:
            #     print(i.values())
            date_val = []
            litr_val = []
            name_val = []
            lv = [[str(i) for i in(i.values())] for i in cur]
            for i in range(len(lv)):
                date_val.append(lv[i][1])
                litr_val.append(lv[i][2])
                name_val.append(lv[i][3])
            for i in range(len(lv)):
                print(date_val[i], '|',
                      litr_val[i], (' '*(len('LitresReset')-len(litr_val[i])-1)),
                      '|', name_val[i])

# UPDATE
# with connection.cursor() as cur:
#     cur.execute('UPDATE reset SET DateReset="2021-12-05" where id="6"')
#     connection.commit()

# DEL
# with connection.cursor() as cur:
#     cur.execute('DELETE from garage where id="52"')
#     connection.commit()

