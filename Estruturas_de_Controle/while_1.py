from random import randint

informed_number = -1
secret_number = randint(0, 10)

while informed_number != secret_number:
    informed_number = int(
        input('Try your luck and enter a number ftom 0 to 10: '))

print('You found out the secret number!!')
