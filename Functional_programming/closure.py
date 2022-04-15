def multiply(x):
    def calc(y):
        return x * y
    return calc


if __name__ == '__main__':
    double = multiply(2)
    triple = multiply(3)
    print(double, triple)
    print(f'The double of 7 is {double(7)}.')
    print(f'The triple of 3 is {triple(3)}.')
