from .people import People
from functools import reduce


class Client(People):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.purchases = []

    def register_purchase(self, purchase):
        self.purchases.append(purchase)

    def get_last_purchase_date(self):
        return None if not self.purchases \
            else sorted(self.purchases,
                        key=lambda purchase: purchase.date)[-1].date

    def total_purchases(self):
        return reduce(lambda p1, p2: p1 + p2,
                      (purchase.value for purchase in self.purchases))
