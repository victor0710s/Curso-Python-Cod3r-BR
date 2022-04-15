# Leitura através de stream pois nao armazena o arquivo
# por completo mas sim usa somente o necessario!

file = open('people.csv')
for register in file:
    print('Name: {}, Age: {}'.format(*register.split(',')))
file.close()
