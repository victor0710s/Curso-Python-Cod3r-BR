# Neste exemplo usaremos o with para simplificar o bloco try/finally

with open('people.csv') as file:
    with open('people.txt', 'w') as output:
        for register in file:
            people = register.strip().split(',')
            print('Name: {}, Age: {}'.format(*people), file=output)

if file.closed:
    print('The file was closed successfully!')

if output.closed:
    print('The output file was closed successfully!')
