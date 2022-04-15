# Implementação simplificada do map:
def mapear(function, list):
    return (function(element) for element in list)


if __name__ == '__main__':
    result = mapear(lambda x: x ** 2, [2, 3, 4])
    print(next(result))
    print(next(result))
    print(next(result))
    print(type(result))
