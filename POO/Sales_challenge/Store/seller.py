from .people import People


class Seller(People):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
