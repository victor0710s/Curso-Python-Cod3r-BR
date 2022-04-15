# Usando o construtor(__init__) neste exemplo

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


# Ex:2
d1 = Data(7, 10, 2002)
# d1.day = 7
# d1.month = 10
# d1.year = 2002
print(d1)
# ----------------------------------------------------
d2 = Data(1, 11, 2004)
# d2.day = 1
# d2.month = 11
# d2.year = 2004
print(d2)
