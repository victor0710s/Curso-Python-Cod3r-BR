generator = (i ** 2 for i in range(10) if i % 2 == 0)


for number in generator:  # Forma mais efivciente que a anterior!
    print(number)
