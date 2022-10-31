""" 13.Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""


if __name__ == '__main__':
    alt = float(input('Digite a altura: '))
    sexo = str.upper(input('Digite o sexo, F - Feminino, M - Masculino: '))

    if sexo == 'M':
        print('O peso ideal é: ', (72.7 * alt) - 58, 'kg')

    elif sexo == 'F':
        print('O peso ideal é: ', (62.1 * alt) - 44.7, 'kg')

    else:
        print('Sexo inválido')