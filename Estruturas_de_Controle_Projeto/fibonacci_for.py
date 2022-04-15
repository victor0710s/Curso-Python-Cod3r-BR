# Substituindo o while pelo for e usando o range:

def fibonacci(amount):
    result = [0, 1]
    for _ in range(2, amount):
        result.append(sum(result[-2:]))
    return result


if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib)
