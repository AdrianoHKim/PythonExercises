""" 24. Faça um Programa que leia 2 números e em seguida pergunte ao
usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a - par ou ímpar;
b - positivo ou negativo;
c - inteiro ou decimal.
"""


if __name__ == '__main__':
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    pergunta = int(input('Digite a operacao que deseja realizar:\n1 - Soma\n2 - Subtração\n'
                         '3 - Multiplicação\n4 - Divisão\n:'))

    resultado = None
    a = 'par'
    b = 'positivo'
    c = 'inteiro'

    if pergunta == 1:
        resultado = n1 + n2
    if pergunta == 2:
        resultado = n1 - n2
    if pergunta == 3:
        resultado = n1 * n2
    if pergunta == 4:
        resultado = n1 / n2
    if resultado % 2 != 0:
        a = 'ímpar'
    if resultado < 0:
        b = 'negativo'
    if resultado != round(resultado):
        c = 'decimal'
    if resultado != str:
        print('O resultado da operação é: ', resultado)
        print('O número é: ', a, ',', b, 'e', c, '.')
