""" 18. Faça um Programa que peça uma data no formato dd/mm/aaaa
e determine se a mesma é uma data válida.
"""


if __name__ == '__main__':
    dia = float(input('Digite o dia: '))
    mes = float(input('Digite o mês: '))
    ano = float(input('Digite o ano: '))
    # lista de meses com 31 dias
    mes31 = [1, 3, 5, 7, 8, 10, 12]
    # lista de meses com 30 dias
    mes30 = [4, 6, 9, 11]

    valida = False

    if mes in mes31:
        if dia <= 31:
            valida = True

    if mes in mes30:
        if dia <= 30:
            valida = True
    # ano bissexto
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if dia <= 29:
                valida = True
        elif dia <= 28:
            valida = True

    if valida:
        print('Data válida')

    else:
        print('Data inválida')
