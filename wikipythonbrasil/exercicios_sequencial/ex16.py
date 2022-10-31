""" 16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
 em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
  a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
  Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
# Obs. usar import math para usar a função math.ceil
# math.ceil é usado para arredondar para o PRÓXIMO número inteiro

import math


if __name__ == '__main__':
    area = float(input('Digite o tamanho em metros da área a ser pintada:'))
    qtde = math.ceil(area/54)
    valor = 80

    if area > 54:
        print('Comprar', math.ceil(area/54), 'lata(s)')
        print('O valor total a ser pago será: ', qtde * valor)

    else:
        print('Comprar apenas 1 lata.')
        print('O valor total a ser pago será: R$ 80.0')
