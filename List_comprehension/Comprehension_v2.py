# [Expressão for item in lista if condicional]

double_pairs = [i * 2 for i in range(10) if i % 2 == 0]
print(double_pairs)


# Versão normal sem o comprehension:

double_pairs_2 = []
for i in range(10):
    if i % 2 == 0:
        double_pairs_2.append(i * 2)
print(double_pairs_2)
