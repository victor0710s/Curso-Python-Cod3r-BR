# Implementação simplificada do map:
def mapear(function, list):
    for element in list:
        yield function(element)


if __name__ == '__main__':
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
