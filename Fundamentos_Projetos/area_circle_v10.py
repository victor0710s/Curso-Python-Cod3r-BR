#! python
from math import pi
import sys  # Sistema


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == "__main__":
    radius = sys.argv[1]  # 0 = nome do arquivo; 1 = segundo argumento
    area = circle(radius)
    print("Area do circulo: ", area)
