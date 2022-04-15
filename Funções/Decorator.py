def log(function):
    def decorator(*args, **kwargs):
        print(f'Start of the function call:{function.__name__ }')
        print(f'args:{args}')
        print(f'kwargs:{kwargs}')
        result = function(*args, **kwargs)
        print(f'Result:{result}')
        return result
    return decorator


@log
def sum(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(sum(5, 7))
    print('------------------')
    print(sub(5, 3))
