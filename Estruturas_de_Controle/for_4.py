# Desafio aula 4 de "for":

# Criar funcao para sortear numeros entre 1 e 6;
# For com range 1 a 6;
# Se o numero for impar continue;
# Se o numero for par e for igual ao valor sorteado print('Acertou!!')
# e depois chamar o break
# Se não acertar, chamar o else... print('Tente novamente!!')

from random import randint

# Função:


def draw_dice():
    return randint(1, 6)


# Laços:
for x in range(1, 7):
    if x % 2 == 1:
        continue

    if draw_dice() == x:
        print('Jackpot!!', x)
        break
else:
    print('Try again later!!')
