from Package_1 import module_1
from Package_2 import module_1 as mod1_sub


if __name__ == '__main__':
    print(module_1.sum(3, 2))
    print(mod1_sub.sub(7, 2))
