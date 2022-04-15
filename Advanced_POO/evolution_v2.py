class Human:
    # atributo de classe
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

    def das_cavernas(self):  # metodo de instancia
        self.specie = 'Homo Neanderthalensis'
        # => economiza uma linha:
        # (objeto = classe('nome ou atributo do obj').das_cavernas)
        return self

    @staticmethod  # metodo estatico
    def species():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco', ) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod  # metodo de classe
    def is_evolved(cls):
        return cls.specie == cls.species()[-1]


class Neandertal(Human):
    specie = Human.species()[-2]


class HomoSapiens(Human):
    specie = Human.species()[-1]


if __name__ == '__main__':
    Victor = HomoSapiens('Victor')
    Grokn = Neandertal('Grokn')
    # Human.das_cavernas(Victor) "outro metodo"

    print(
        f'Evolved (a partir da classe): {", ".join(HomoSapiens.species())}')
    print(f'Evolved (a partir da instancia): {", ".join(Victor.species())}')
    print(f'Homo Sapiens evolved?: {HomoSapiens.is_evolved()}')
    print(f'Homo Neanderthalensis evolved?: {Neandertal.is_evolved()}')
    print(f'Victor evolved?: {Victor.is_evolved()}')
    print(f'Grokn evolved?: {Grokn.is_evolved()}')
# a partir da classe,
#  o metodo de classe recebe como primeiro parametro a classe e
# a partir da instancia, recebe a instancia e metodo estatico nao recebe nada
