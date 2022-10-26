""" 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""


if __name__ == '__main__':
    numero = int(input('Digite um numero: '))

    divisores = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
                break

    if divisores > 1 or numero == 1 or numero == 0:
        print('O numero não é primo.')

    else:
        print('O numero é primo.')
