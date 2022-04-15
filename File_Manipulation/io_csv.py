# Usando Modulo csv

import csv

with open('people.csv') as entry:
    for people in csv.reader(entry):
        print('Name: {}, Age: {}'.format(*people))
