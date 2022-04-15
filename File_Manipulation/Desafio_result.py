# Extrair o nono e o quarto campos do arquivo csv
# O desafio foi feito correto mas nao é possivel abrir o arquivo,
# pois o link deve estar com problema!!

import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entry:
        print('Downloading cvs file...')
        data = entry.read().decode('latin1')
        print('Download completed!!')
        for city in csv.reader(data.splitlines()):
            print(f'{city[8]}: {city[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
