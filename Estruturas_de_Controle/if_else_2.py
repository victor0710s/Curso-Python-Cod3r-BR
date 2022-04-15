# Assim como na versao anterior iremos fazer um projeto
# onde uma função determinará a faixa etária da pessoa e
# de acordo com a idade da mesma.


# Função :

def age_group(age):
    if 0 <= age < 18:
        return 'Minor'

    elif age in range(18, 50):
        return 'Adult'
    elif age in range(50, 100):
        return 'Best age'
    elif age >= 100:
        return 'Centenary'

    else:
        return 'Invalid Age!!'


if __name__ == '__main__':
    for age in (17, 34, 42, 65, 113, -4):
        print(f'{age}: {age_group(age)}')
