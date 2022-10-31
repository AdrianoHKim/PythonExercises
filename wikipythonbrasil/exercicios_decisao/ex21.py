""" 21. Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e
depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

import math


if __name__ == '__main__':
    val = int(input('Digite o valor do saque (Valor mínimo = R$ 10 | Valor máximo = R$ 600) : '))

    cem = int(math.floor(val/100))
    cinquenta = int(math.floor((val % 100)/50))
    dez = int(math.floor((val % 50)/10))
    cinco = int(math.floor((val % 10)/5))
    um = int(math.floor(val % 5)/1)

    if val < 10 or val > 600:
        print('Valor inválido, reinicie o procedimento.')
        exit()

    else:
        print('== Saque efetuado com sucesso, retire as notas ==')
        print('Notas de R$ 100: ', cem)
        print('Notas de R$ 50: ', cinquenta)
        print('Notas de R$ 10: ', dez)
        print('Notas de R$ 5: ', cinco)
        print('Notas de R$ 1: ', um)
