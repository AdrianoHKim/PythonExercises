""" 1. Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

para um n informado pelo usuário.
Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""


if __name__ == '__main__':
    def ex1(n):
        for i in range(n):
            i += 1
            print(f'{i}  ' * i)


    num = int(input('Digite um numero: '))

    ex1(num)
