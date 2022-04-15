class HtmToStringMixin:
    def __str__(self):
        # Conversão para HTML
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>') \

        return f'<span>{html}</span>'


class People:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Animal:
    def __init__(self, name, pet=True):
        self.name = name
        self.pet = pet

    def __str__(self):
        return self.name + ' (pet)' if self.pet else ''


class PeopleHtml(HtmToStringMixin, People):
    pass


class AnimalHtml(HtmToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = People('Maria')
    print(p1)

    p2 = PeopleHtml('Victor')
    print(p2)

    Totó = AnimalHtml('Toto')
    print(Totó)
