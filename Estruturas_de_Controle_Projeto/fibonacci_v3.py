# Fibonacci = a soma do penultimo + ultimo
# ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.....

# Na 3ª versão iremos simplificar fazendo um switch das var.:

def fibonacci(limit):
    penultimate = 0
    ultimate = 1
    print(f'{penultimate}, {ultimate}', end=',')
    while ultimate < limit:
        penultimate, ultimate = ultimate, penultimate + ultimate
        print(ultimate, end=',')


if __name__ == '__main__':
    fibonacci(10000)
