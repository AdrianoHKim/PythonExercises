""" 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""


if __name__ == '__main__':
    num = float(input('Digite o número: '))

    if num != round(num):
        print('O número é decimal')

    else:
        print('O número é inteiro.')
