""" 8. Faça um programa que pergunte o preço de três produtos e
informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""


if __name__ == '__main__':
    p1 = float(input('Digite o preço do primeiro produto: '))
    p2 = float(input('Digite o preço do segundo produto: '))
    p3 = float(input('Digite o preço do terceiro produto: '))

    lista = [p1, p2, p3]
    lista2 = sorted(lista)

    print('Comprar o produto com o valor de : R$ ', lista2[0])
