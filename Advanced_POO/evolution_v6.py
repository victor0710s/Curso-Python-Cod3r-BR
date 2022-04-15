from abc import ABCMeta, abstractproperty


class Human(metaclass=ABCMeta):
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    @abstractproperty
    def intelligent(self):
        raise NotImplementedError('Abstract Property')

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

    @property
    def intelligent(self):
        return False


class HomoSapiens(Human):
    specie = Human.species()[-1]

    @property
    def intelligent(self):
        return True


if __name__ == '__main__':

    try:
        Anonymous = Human('Elon Musk')
        print(Anonymous.intelligent)
    except TypeError:
        print("Abstract Class can't be instanciate('Chamada')!!")

    Victor = HomoSapiens('Victor')
    print('{} of the {} class, intelligent = {}'
          .format(Victor.name, Victor.__class__.__name__, Victor.intelligent))
    Grokn = Neandertal('Grokn')
    print('{} of the {} class, intelligent = {}'
          .format(Grokn.name, Grokn.__class__.__name__, Grokn.intelligent))
