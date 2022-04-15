from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Mudar linguagem para o PT-BR
setlocale(LC_ALL, 'pt-BR')

# Listar todos os meses do ano com 31 dias


def month_31(month):
    return mdays[month] == 31


def get_month_name(month):
    return month_name[month]


def join_all(all, month_name):
    return f'{all}\n- {month_name}'


print(reduce(join_all,
             map(get_month_name, filter(month_31, range(1, 13))),
             'Months with 31 days: '))
