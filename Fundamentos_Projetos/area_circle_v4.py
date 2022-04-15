#! python
from math import pi
# O 'from' é utilizado quando se quer importar uma única
# funcionalidade de uma determinada biblioteca.

print(dir())

# Quando invocamos o comando dir(),
# passando como argumento a tal comando um objeto,
# este irá retornar uma lista de strings contendo os nomes das funções e
# dos atributos disponíveis para tal tipo de objeto

radius = 5.1
print('Area circulo: ', pi * radius ** 2)
