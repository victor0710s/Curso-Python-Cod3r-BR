# **kwargs

def result_f1(**podium):
    for position, pilot in podium.items():
        print(f'{position} -> {pilot}')


if __name__ == '__main__':
    result_f1(First='L. Hemilton',
              Second='S. Vettel',
              Third='M. Verstappen')
