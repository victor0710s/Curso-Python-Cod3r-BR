def get_type_days(day):
    days = {
        (1, 7): 'Weekend',
        tuple(range(2, 7)): 'Days of week'
    }
    chosen_day = (tipo for numbers, tipo in days.items() if day in numbers)
    return next(chosen_day, '** Invalid Day **')


if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {get_type_days(day)}')
