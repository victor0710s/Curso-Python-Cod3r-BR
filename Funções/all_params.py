def all_params(*args, **kwargs):
    print(f'args:{args}')
    print(f'kwargs:{kwargs}')


if __name__ == '__main__':
    all_params('a', 'b', 'c')
    print('------------------')
    all_params(1, 2, 3, cool=True, value=12.5)
    print('------------------')
    all_params('Ana', False, [1, 2, 3], Size='M', fragile=False)
    print('------------------')
    all_params(First='Jonh', Second='Maria')
    print('------------------')
    all_params('Maria', First='Jonh')
