# Nesta aula iremos fazer um código simulando o switch do java
# que não tem de forma nativa no python:

def get_days_week(day):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thirsday',
        6: 'Friday',
        7: 'Saturday'
    }
    return days.get(day, '** Invalid day **')


if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {get_days_week(day)}')
