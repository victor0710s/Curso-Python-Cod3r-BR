def execute(function):
    function()


def good_moorning():
    print('Good Moorning!')


def good_evening():
    print('Good Evening!')


if __name__ == '__main__':
    execute(good_moorning)
    execute(good_evening)
    execute(1)  # Vai dar erro pois "1" nao é uma função!
