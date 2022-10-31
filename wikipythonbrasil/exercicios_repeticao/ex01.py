""" 1. Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""


if __name__ == '__main__':
    nota = int(input('Digite uma nota de 0 a 10: '))

    while nota > 10 or nota < 0:
        print('Nota invalida! ')
        nota = int(input('Informe uma nota de 0 a 10: '))
    else:
        print('Nota validada com sucesso! ')
