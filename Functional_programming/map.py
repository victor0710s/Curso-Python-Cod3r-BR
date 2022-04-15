list_1 = [1, 2, 4]

double = map(lambda x: x * 2, list_1)
print(list(double))

list_2 = [
    {'Name': 'Joao', 'Age': 31},
    {'Name': 'Maria', 'Age': 37},
    {'Name': 'Jose', 'Age': 26}
]

just_names = map(lambda p: p['Name'], list_2)
print(list(just_names))
just_age = map(lambda p: p['Age'], list_2)
print(sum(just_age))

# Desafio: Retornar uma frase do tipo '<Nome> tem <Idade> anos' usando o map

challenge = map(lambda p: f'{p["Name"]} tem {p["Age"]} anos.', list_2)
print(list(challenge))
