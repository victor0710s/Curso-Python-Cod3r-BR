#! python
from math import pi
import sys  # Sistema
import errno


def help():
    print("É necessário informar o raio do circulo!!")
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():  # Se o dado não for numérico
        help()
        print("O raio deve ser um valor numérico!!")
        sys.exit(errno.EINVAL)

    radius = sys.argv[1]
    area = circle(radius)
    print("Area do circulo: ", area)
