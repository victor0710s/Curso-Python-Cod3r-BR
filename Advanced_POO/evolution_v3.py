class Human:
    # atributo de classe
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None  # _atributo privado

    # ** agore iremos usar dois metodos pra setar e pegar a idade
    def get_age(self):  # Le o valor de um atributo
        return self._age

    def set_age(self, age):  # altera o valor de um atributo
        if age < 0:
            raise ValueError('Age must be a positive number!!')
        self._age = age

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
    Victor.set_age(19)
    print(f'Name: {Victor.name}// Age: {Victor.get_age()}')
    print(f'Name: {Victor.name}// Age: {Victor._age}')
    # _age pode ser usado assim para pegar a idade,
    # mas não é o metodo correto pois com o '_' vira um atributo privado

    print(f'Name: {Victor.name}// Age: {Victor.get_age()}')
