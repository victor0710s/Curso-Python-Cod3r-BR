# Fibonacci = a soma do penultimo + ultimo
# ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.....

# Na 2ª versão iremos adicionar um limite ao codigo

def fibonacci(limit):
    penultimate = 0
    ultimate = 1
    print(f'{penultimate}, {ultimate}', end=',')
    while ultimate < limit:
        next = penultimate + ultimate
        print(next, end=',')
        penultimate = ultimate
        ultimate = next


if __name__ == '__main__':
    fibonacci(10000)
