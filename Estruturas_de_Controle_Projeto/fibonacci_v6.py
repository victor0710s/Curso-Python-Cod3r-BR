# Na 4ª versão iremos trocar as variaveis por lista:


def fibonacci(amount):
    result = [0, 1]
    while True:
        result.append(sum(result[-2:]))
        if len(result) == amount:
            break
    return result


if __name__ == '__main__':
    # listar os 10 primeiros numeros:
    for fib in fibonacci(10):
        print(fib)
