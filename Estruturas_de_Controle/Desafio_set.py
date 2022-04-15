FORBIDDEN_WORDS = {'futebol', 'religion', 'politics'}
texts = [
    'Jonh likes futebol and politics',
    'The beach was fun'
]

for text in texts:
    intersection = FORBIDDEN_WORDS.intersection(set(text.lower().split()))
    if intersection:
        print('The text has at least one forbidden words:', intersection)
    else:
        print('The text has been approved:', text)
