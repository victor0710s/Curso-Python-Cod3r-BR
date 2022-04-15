people = [
    {'name': 'Pedro', 'age': 11},
    {'name': 'Mariana', 'age': 18},
    {'name': 'Arthur', 'age': 26},
    {'name': 'Rebeca', 'age': 6},
    {'name': 'Tiago', 'age': 19},
    {'name': 'Gabriela', 'age': 17},
]

underage = filter(lambda x: x['age'] < 18, people)
print(list(underage))


carac = filter(lambda x: len(x['name']) >= 7, people)
print(tuple(carac))
