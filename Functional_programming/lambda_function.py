purchases = (
    {'qnt': 2, 'price': 10},
    {'qnt': 3, 'price': 20},
    {'qnt': 5, 'price': 14}
)

totals = tuple(
    map(lambda purchase: purchase['qnt'] * purchase['price'],
        purchases)
)

print('Total prices:', totals)
print('Total:', sum(totals))
