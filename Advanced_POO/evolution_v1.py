class Human:
    # atributo de classe
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

    def das_cavernas(self):
        self.specie = 'Homo Neanderthalensis'
        # => economiza uma linha:
        # (objeto = classe('nome ou atributo do obj').das_cavernas)
        return self


if __name__ == '__main__':
    Victor = Human('Victor')
    Grokn = Human('Grokn').das_cavernas()

    print(f'Human.specie = {Human.specie}')
    print(f'Victor.specie = {Victor.specie}')
    print(f'Grokn.specie = {Grokn.specie}')
