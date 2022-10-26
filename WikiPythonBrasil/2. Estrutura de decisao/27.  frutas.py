""" 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e
a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""


if __name__ == '__main__':
    mor = float(input('Digite a quantidade em kg de morangos: '))
    mac = float(input('Digite a quantidade em kg de maçã: '))

    mop = 2.5
    map = 1.8

    mony = '{:.2f}'.format

    if mor + mac > 8 or ((mor * mop) + (mac * map)) > 25:
        if mor > 5:
            mop = 2.2
        if mac > 5:
            map = 1.5
        print('Valor total a ser pago: R$', mony((((mor * mop) + (mac * map)) * 0.9)))

    else:
        if mor > 5:
            mop = 2.2
        if mac > 5:
            map = 1.5
        print('Valor total a ser pago: R$', mony((mor * mop) + (mac * map)))
