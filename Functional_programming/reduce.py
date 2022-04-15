from functools import reduce

people = [
    {'name': 'Pedro', 'age': 11},
    {'name': 'Mariana', 'age': 18},
    {'name': 'Arthur', 'age': 26},
    {'name': 'Rebeca', 'age': 6},
    {'name': 'Tiago', 'age': 19},
    {'name': 'Gabriela', 'age': 17},
]

just_age = map(lambda x: x['age'], people)  # Pega somente as idades
underage = filter(lambda age: age < 18, just_age)  # Filtra idades abaixo de 18
sum_age = reduce(lambda ages, age: ages + age, underage, 0)  # Soma as idades
print(sum_age)
