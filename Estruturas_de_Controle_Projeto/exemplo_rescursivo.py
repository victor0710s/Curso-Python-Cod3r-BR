def imprint(max, actual):
    if actual >= max:
        return
    print(actual)
    imprint(max, actual + 1)


imprint(10, 1)
