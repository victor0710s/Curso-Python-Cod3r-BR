# Leitura através de stream pois nao armazena o arquivo
# por completo mas sim usa somente o necessario!
# Usaremos o .strip para eliminar os espacos em brancos desnecessarios!

try:
    file = open('people.csv')

    for register in file:
        print('Name: {}, Age: {}'.format(*register.strip().split(',')))
finally:
    print('Finally')
    file.close()

if file.closed:
    print('The file was closed successfully!')
