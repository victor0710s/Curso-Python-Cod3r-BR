from first_class_function import double, square


def process(title, lists, function):
    print(f'Processing: {title}')
    for i in lists:
        print(i, '=>', function(i))


if __name__ == '__main__':
    process('Double from 1 to 10', range(1, 11), double)
    process('Square from 1 to 10', range(1, 11), square)
