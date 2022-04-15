#! python
# Nessa versão foi adicionada uma atualização estética para o terminal
from math import pi
import sys  # Sistema
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'
    RESULT = '\033[1;32m'
    AVISO = '\033[1;33m'


def help():
    print(TerminalColor.AVISO +
          "É necessário informar o raio do circulo!!" +
          TerminalColor.NORMAL)
    print(TerminalColor.AVISO +
          "Sintaxe: {} <raio>".format(sys.argv[0]) +
          TerminalColor.NORMAL)


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():  # Se o dado não for numérico
        help()
        print(
            TerminalColor.ERRO +
            "O raio deve ser um valor numérico!!" +
            TerminalColor.NORMAL
        )
        sys.exit(errno.EINVAL)

    radius = sys.argv[1]
    area = circle(radius)
    print(
        TerminalColor.RESULT + "Area do circulo: {}".format(area) +
        TerminalColor.NORMAL
    )
