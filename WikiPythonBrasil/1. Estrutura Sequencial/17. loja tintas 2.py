""" 17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
 em metros quadrados da área a ser pintada. Considere que a cobertura
 da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
 latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

import math


if __name__ == '__main__':
    lat1 = float(108)
    lat2 = float(21.6)

    area = float(input('Digite o tamanho da área em metros: '))

    print('= USANDO APENAS LATAS DE 18 LITROS =')
    print('Quantidade de latas de 18 litros: ', math.ceil((area * 1.1)/lat1))
    print('Valor a ser pago pelas latas de 18 litros: ', 'R$', (math.ceil((area * 1.1)/lat1)) * 80)

    print('= USANDO APENAS GALÕES DE 3.6 LITROS =')
    print('Quantidade de galões de 3.6 litros: ', math.ceil((area * 1.1)/lat2))
    print('Valor a ser pago pelos galões de 3.6 litros: ', 'R$', (math.ceil((area * 1.1)/lat2)) * 25)


    print('= USANDO LATAS E GALÕES =')

    a1 = math.trunc((area * 1.1)/lat1)
    a2 = (area * 1.1) % lat1
    a3 = math.ceil(a2/lat2)
    a4 = ((a1 * 80) + (a3 * 25))

    print('Quantidade de latas de 18 litros: ', a1)
    print('Quantidade de galôes de 3.6 litros: ', a3)
    print('Valor total a ser pago pelas latas e galões: ', a4)
