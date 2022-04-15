#! python
from math import pi

# 3.1) Após chamar a função e fazer o passo a passo,
#      sera imprimido a resolução da mesma 'v'


def circle(radius):
    print('Area circulo: ', pi * float(radius) ** 2)


if __name__ == "__main__":  # 1ª) Condição do modulo
    # 2ª) Coletar dados do usuário
    radius = input('Inform the circle radius: ')
    circle(radius)  # 3ª) Chama a função
