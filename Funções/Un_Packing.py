def sum_1(a, b):
    return a + b


def sum_2(a, b, c):
    return a + b + c


def sum_n(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


if __name__ == '__main__':
    # Exemplo de packing
    print(sum_1(2, 3))
    print(sum_2(2, 5, 7))
    print(sum_n(1, 2, 3, 4, 5))

    # Exemplo de Unpacking
    tuple_nums = (1, 2, 3, 4)
    print(sum_n(*tuple_nums))

    list_nums = [1, 2, 3, 4, 5]
    print(sum_n(*list_nums))
