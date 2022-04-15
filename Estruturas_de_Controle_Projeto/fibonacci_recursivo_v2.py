#  Desafio: Fibonacci recursivo seguindo os exeplos da aula

def fibonacci(amount, seq=(0, 1)):
    # Condição de Parada:
    return seq if len(seq) == amount else \
        fibonacci(amount, seq + (sum(seq[-2:]),))


if __name__ == "__main__":
    # listar os 20 primeiros numeros da repetição!
    for fib in fibonacci(20):
        print(fib)
