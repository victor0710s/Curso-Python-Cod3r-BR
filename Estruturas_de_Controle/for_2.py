# Nesta versão usaremos o 'for' para percorrer as letras de uma string'':

word = 'python'
for letter in word:
    print(letter, end=',')
print('Fim')
# Ao colocar o parametro nominal "end",
# conseguimos fazer com que as letras sejam separadas por linhas
# e não por colunas.
print('----------------------------------')  # separar no output

# Logo abaixo usaremos o 'for em um dicionario[] e ele terá a mesma função :

approveds = ['Luna', 'Daphne', 'Geovana', 'Sophia', 'Rebecca']
for name in approveds:
    print(name)
print('----------------------------------')

for position, name in enumerate(approveds):
    print(f'{position + 1})', name)
print('----------------------------------')

# Logo abaixo usaremos o 'for em uma tupla():

days_week = ('Sunday', 'Monday', 'Tuesday',
             'Wednesday', 'Thursday', 'Friday', 'Saturday')
for day in days_week:
    print(f'Today is {day}')
print('----------------------------------')

# Logo abaixo usaremos o 'for' em um 'set':

for letter in set('muito legal'):
    print(letter)
# O set nesse caso irá mostrar a ordem sendo ela ordenada ou não
# não há garantia que poderá vir ordenada sendo uma string''.
