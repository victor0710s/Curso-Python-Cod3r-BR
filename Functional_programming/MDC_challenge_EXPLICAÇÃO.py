def mdc(numbers):  # 1
    def calc(divisor):  # 2
        return divisor if sum(map(lambda x: x % divisor, numbers))\
            == 0 else calc(divisor - 1)  # 3
    return calc(min(numbers))  # 4


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1


# 1 = Lista de numeros

# 2 = Menor numero que ser usado como divisor e o
# mesmo estara dentro da lista de numeros

# 3 = A função vai pegar cada valor da lista e vai dividir por pelo divisor e
# caso nao dê 0, será subtraido 1 do valor do divisor
# ate a soma desta divisao dar 0

# 4 = Vai pegar o menor numero da lista e
# vai usar ele como primeiro candidato a ser o MDC na função calc
