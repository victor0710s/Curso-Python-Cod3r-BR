from locale import setlocale, LC_ALL
from calendar import mdays, month_name

# Mudar linguagem para o PT-BR
setlocale(LC_ALL, 'pt-BR')

# Listar todos os meses com 31 dias.
print('Meses com 31 dias: ')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'-{month_name[mes]}')
