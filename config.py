host = 'localhost'
user = 'root'
password = 'Cdtnjxrf86'
name = 'diesel'
import datetime

# surnames = 'Титов,Алексеев,Савельев,Черкасов,Юрьев,Сажнев,Авилочкин,Дильдин,Усачев,Кизиль,Бирюков,Жирнов,' \
#            'Пустынников,Назин'.split(',')

a = {'id': 13, 'date_': datetime.date(2021, 10, 1), 'liters': 30, 'id_driver': 10}

def razbor(arg):
    keys = [i for i in arg.keys()]
    values = [str(i) for i in arg.values()]
    str_keys = ' | '.join(keys)
    print(str_keys)
    print('-' * len(str_keys))
    print(' | '.join(values))

    # print(keys)
    # print('-'*35)
    # print(values)

razbor(a)