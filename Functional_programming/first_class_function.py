def double(x):
    return x * 2


def square(x):
    return x ** 2


if __name__ == '__main__':
    # retornar o dobro e o quadro de 1 ate 10
    funcs = [double, square] * 5
    for func, numbers in zip(funcs, range(1, 11)):
        print(f'The {func.__name__} of {numbers} is {func(numbers)}')
