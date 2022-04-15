class Human:
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    # este metodo faz com que a idade seja passada como uma "variavel"
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('Age must be a positive number!!')
        self._age = age

    def das_cavernas(self):
        self.specie = 'Homo Neanderthalensis'

        return self

    @staticmethod
    def species():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco', ) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evolved(cls):
        return cls.specie == cls.species()[-1]


class Neandertal(Human):
    specie = Human.species()[-2]


class HomoSapiens(Human):
    specie = Human.species()[-1]


if __name__ == '__main__':
    Victor = HomoSapiens('Victor')
    Victor.age = 19  # acessado como uma variavel/atributo de instacia.
    print(f'Name: {Victor.name}// Age: {Victor.age}')
