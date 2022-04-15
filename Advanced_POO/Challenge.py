class SimpleClasses:
    contador = 0

    def __init__(self):
        self.__class__.contador += 1


if __name__ == '__main__':
    lista = [SimpleClasses(), SimpleClasses()]
    print(SimpleClasses.contador)  # esperado 2
