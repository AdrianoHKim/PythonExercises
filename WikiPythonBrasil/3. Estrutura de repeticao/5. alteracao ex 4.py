""" 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""


if __name__ == '__main__':
    print('Siga a regra de que a cidade A deve ser a cidade com menor populacao: ')
    a = float(input('Digite a populacao da cidade A: '))
    cresc_a = float(input('Digite a taxa de crescimento da cidade A, em %: '))
    b = float(input('Digite a populacao da cidade B: '))
    cresc_b = float(input('Digite a taxa de crescimento da cidade B, em %: '))
    ano = 0

    while a <= b:
        a += a * (cresc_a / 100)
        b += b * (cresc_b / 100)
        ano += 1
    print('A cidade A ultrapassa ou iguala a B em %d ano(s)' % ano)
    resp = str.upper(input('Dados validados com sucesso!\nDeseja repetir a operacao?\n(S/N): '))

    while resp == 'S':
        print('Siga a regra de que a cidade A deve ser a cidade com menor populacao: ')
        a = float(input('Digite a populacao da cidade A: '))
        cresc_a = float(input('Digite a taxa de crescimento da cidade A, em %: '))
        b = float(input('Digite a populacao da cidade B: '))
        cresc_b = float(input('Digite a taxa de crescimento da cidade B, em %: '))
        ano = 0

        while a <= b:
            a += a * (cresc_a / 100)
            b += b * (cresc_b / 100)
            ano += 1
        print('A cidade A ultrapassa ou iguala a B em %d ano(s)' % ano)
        resp = str.upper(input('Dados validados com sucesso!\nDeseja repetir a operacao?\n(S/N): '))
