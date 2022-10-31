""" 12.Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""


if __name__ == '__main__':
    alt = float(input('Digite a altura em metros: '))

    print('O peso ideal é: ', round((72.7 * alt) - 58), 'kg')
