#!/usr/bin/env python3

import sys
from random import randint


def gabarito(questoes, alternativas):

    A = 65
    
    digitos = len(str(questoes))
    formato = '%' + str(digitos) + 'd'

    for questao in range(1, questoes + 1):

        alternativa = randint(0, alternativas)
        letra = chr(A + alternativa)

        print(formato % questao, letra)


if __name__ == '__main__':

    questoes, alternativas = 10, 5

    if len(sys.argv) > 1:
        questoes = int(sys.argv[1])

    if len(sys.argv) > 2:
        alternativas = int(sys.argv[2])

    gabarito(questoes, alternativas)

