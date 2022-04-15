products = {'Name': 'Hyperx Fury', 'Price': 280.00,
            'Imported': True, 'Inventory': 198}

for key in products:
    print(key)
print('----------------------------------')

for value in products.values():
    print(value)
print('----------------------------------')

for key, value in products.items():
    print(key, '=', value)
