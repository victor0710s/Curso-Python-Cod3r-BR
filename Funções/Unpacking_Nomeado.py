# **kwargs

def result_f1(First, Second, Third):
    print(f'1º) {First}')
    print(f'2º) {Second}')
    print(f'3º) {Third}')


if __name__ == '__main__':
    podium = {'First': 'L. Hemilton',
              'Second': 'S. Vettel',
              'Third': 'M. Verstappen'}

    result_f1(**podium)
