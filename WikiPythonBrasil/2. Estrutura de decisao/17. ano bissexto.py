""" 17. Faça um Programa que peça um número correspondente a um
determinado ano e em seguida informe se este ano é ou não bissexto.
"""


if __name__ == '__main__':
    ano = float(input('Digite o ano: '))

    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print('O ano é bissexto.')
    else:
        print('Não é um ano bissexto.')
