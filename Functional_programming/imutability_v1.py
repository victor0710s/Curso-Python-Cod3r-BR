from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Mudar linguagem para o PT-BR
setlocale(LC_ALL, 'pt-BR')

# Listar todos os meses do ano com 31 dias
days = filter(lambda x: mdays[x] == 31, range(1, 13))
months = map(lambda i: month_name[i], days)
result = reduce(lambda all, month_names: f'{all}\n- {month_names}',
                months, 'Meses com 31 dias:')

print(result)
