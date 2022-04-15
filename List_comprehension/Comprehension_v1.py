# [Expressão for item in lista if condicional]

double = [i * 2 for i in range(10)]
print(double)

# Versão normal sem o comprehension:

double = []
for i in range(10):
    double.append(i * 2)
print(double)
