# Fibonacci = a soma do penultimo + ultimo
# ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.....

def fibonacci():
    penultimate = 0
    ultimate = 1
    print(f'{penultimate}, {ultimate}', end=',')
    while True:
        next = penultimate + ultimate
        print(next, end=',')
        penultimate = ultimate
        ultimate = next


if __name__ == '__main__':
    fibonacci()
