# Neste exemplo usaremos o with para simplificar o bloco try/finally

with open('people.csv') as file:
    for register in file:
        print('Name: {}, Age: {}'.format(*register.strip().split(',')))

if file.closed:
    print('The file was closed successfully!')
