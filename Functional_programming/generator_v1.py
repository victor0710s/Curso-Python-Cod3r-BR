def rainbow_colors():
    yield 'Red'
    yield 'Orange'
    yield 'Yellow'
    yield 'Green'
    yield 'Blue'
    yield 'Indigo'
    yield 'Violet'


if __name__ == '__main__':
    generator = rainbow_colors()
    print(type(generator))
    while True:
        print(next(generator))
