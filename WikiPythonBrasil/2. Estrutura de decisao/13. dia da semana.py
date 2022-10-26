""" 13. Faça um Programa que leia um número e exiba o dia correspondente da semana.
 (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
 """


if __name__ == '__main__':
    dia = float(input('Digite o número: '))

    if dia == 1:
        print('1-Domingo')

    elif dia == 2:
        print('2-Segunda')

    elif dia == 3:
        print('3-Terça')

    elif dia == 4:
        print('4-Quarta')

    elif dia == 5:
        print('5-Quinta')

    elif dia == 6:
        print('6-Sexta')

    elif dia == 7:
        print('7-Sábado')

    else:
        print('Valor inválido')
