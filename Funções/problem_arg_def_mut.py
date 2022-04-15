def fibonacci(sequence=[0, 1]):
    sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == '__main__':
    start = fibonacci()
    print(start, id(start))
    print(fibonacci(start))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
