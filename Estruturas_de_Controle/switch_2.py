# Desafio de fazer uma função identificar um dia da semana
# e um dia do fim de semana:

def identify_days(day):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thirsday',
        6: 'Friday',
        7: 'Saturday'
    }
    return days.get(day)


if __name__ == '__main__':
    for day in range(1, 8):
        if day == 1 or day == 7:
            print(f'{identify_days(day)}: Weekend')

        else:
            if day in range(2, 7):
                print(f'{identify_days(day)}: Weekdays')
