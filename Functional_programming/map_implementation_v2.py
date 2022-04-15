# Implementação simplificada do map:
def mapear(function, list):
    # Lazy evaluation:
    for element in list:
        print("I'm Here...")
        yield function(element)


if __name__ == '__main__':
    result = mapear(lambda x: x ** 2, [2, 3, 4])
    print(next(result))
    print(next(result))
    print(next(result))
    print(type(result))
