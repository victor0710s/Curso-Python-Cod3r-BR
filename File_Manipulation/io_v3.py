# Leitura através de stream pois nao armazena o arquivo
# por completo mas sim usa somente o necessario!
# Usaremos o .strip para eliminar os espacos em brancos desnecessarios!

file = open('people.csv')
for register in file:
    print('Name: {}, Age: {}'.format(*register.strip().split(',')))
file.close()
