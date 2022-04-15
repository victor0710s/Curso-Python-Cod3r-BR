purchases = (
    {'qnt': 2, 'price': 10},
    {'qnt': 3, 'price': 20},
    {'qnt': 5, 'price': 14}
)


def calc_total_ptice(purchase):
    return purchase['qnt'] * purchase['price']


totals = tuple(map(calc_total_ptice, purchases))

print('Total prices:', totals)
print('Total:', sum(totals))
