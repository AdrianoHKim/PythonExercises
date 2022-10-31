""" 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""


if __name__ == '__main__':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))

    print('a. Produto do dobro do primeiro com metade do segundo: ', (n1 * 2) / (n2/2))
    print('b. A soma do triplo do primeiro com o terceiro: ', (n1 * 3) + n3)
    print('c. O terceiro elevado ao cubo: ', n3 ** 3)
