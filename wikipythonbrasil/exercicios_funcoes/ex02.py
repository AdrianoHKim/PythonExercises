""" 2. Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário.
Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


if __name__ == '__main__':
    def contagem(n):
        for x in range(n):
            x += 1
            for i in range(x):
                i += 1
                print(f'{i}', end='  ')
            print('')


    numero = int(input('Digite um numero: '))

    contagem(numero)
