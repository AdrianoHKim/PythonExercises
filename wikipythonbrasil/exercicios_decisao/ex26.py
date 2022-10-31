""" 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se
 que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
 """


if __name__ == '__main__':
    litro = float(input('Digite a quantidade de litros: '))
    tipo = str.upper(input('Digite o tipo de combustível | A-álcool | G-gasolina : '))


    if tipo == 'A':
        if litro > 20:
            print('Preço a ser pago: R$', (litro * 1.9) * 0.95)
        else:
            print('Preço a ser pago: R$', (litro * 1.9) * 0.97)

    elif tipo == 'G':
        if litro > 20:
            print('Preço a ser pago: R$', (litro * 2.5) * 0.94)
        else:
            print('Preço a ser pago: R$', (litro * 2.5) * 0.96)

    else:
        print('Tipo de combustível inválido!')
