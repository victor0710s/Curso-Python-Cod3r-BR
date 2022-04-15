OlderAge = 18


class People(object):
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        if not self.age:
            return self.name

        return f'{self.name} ({self.age} years)'

    def is_Adult(self):
        return (self.age or 0) > OlderAge
