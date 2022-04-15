from functools import reduce
from operator import add

valores = (30, 25, 10, 70, 100, 94)

print(sorted(valores))
# valores.sort()
# print(valores)
# Ao chamar uma função dentro de uma lista como anteriormente, o valor da
# mesma será mudado
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(tuple(reversed(valores)))
print(valores)

valores.reversed()  # Chamada de funcao dentro da lista = mudança de valores
print(valores)
