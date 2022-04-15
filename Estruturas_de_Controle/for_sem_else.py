FORBIDDEN_WORDS = ('futebol', 'religion', 'politics')
texts = [
    'Jonh likes futebol and politics',
    'The beach was fun'
]


for text in texts:
    found = False
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print('The text has at least one forbidden words:', word)
            found = True
            break

    if not found:
        print('The text has been approved:', text)
