# Conceitos    Notas
# A            De 10 à 9,1
# A-           De 9 à 8,1
# B            De 8 à 7,1
# B-           De 7 à 6,1
# C            De 6 à 5,1
# C-           De 5 à 4,1
# D            De 4 à 3,1
# D-           De 3 à 2,1
# E            De 2 à 1,1
# E-           De 1 à 0,0

# Para notas maiores que 10 e menores do que 0 será impresso "Nota Inválida."

# Funções
def note_concept(value):
    note = float(value)

    if note > 10:
        return 'Invalid Note!'

    elif note >= 9.1:
        return 'A'
    elif note >= 8.1:
        return 'A-'
    elif note >= 7.1:
        return 'B'
    elif note >= 6.1:
        return 'B-'
    elif note >= 5.1:
        return 'C'
    elif note >= 4.1:
        return 'C-'
    elif note >= 3.1:
        return 'D'
    elif note >= 2.1:
        return 'D-'
    elif note >= 1.1:
        return 'E'
    elif note >= 0.0:
        return 'E-'

    else:
        return 'Invalid Note!'


# Resolução
if __name__ == '__main__':
    value_informed = input('Enter student grade: ')
    concept = note_concept(value_informed)
    print('Concept:', concept)
