#! python
from math import pi


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == "__main__":
    radius = input('Inform the circle radius: ')
    area = circle(radius)  # explicação 1
    print("Area do circulo: ", area)

# 1. Como a função vai retornar um valor,
# iremos armazenar esse valor em uma variavél.
