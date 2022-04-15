class Potency:
    def __init__(self, exp):
        self.exp = exp

    def __call__(self, base):
        return base ** self.exp


if __name__ == '__main__':
    Squared = Potency(2)
    Cubed = Potency(3)

    if callable(Squared) and callable(Cubed):
        print(f'3² =>{Squared(3)}')  # Somente o valor da base!
        print(f'5³ =>{Cubed(5)}')  # Somente o valor da base!
        print(f'3² =>{Potency(2)(3)}')  # Primeiro o exp e depois a base!
