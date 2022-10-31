""" 10. Número por extenso.
Escreva um programa que solicite ao usuário a digitação de um número até 99 e
 imprima-o na tela por extenso.
 """


def converter_em_texto(numeral1):
    dicionario_numerico = {
        0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
        16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
        30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
        80: 'oitenta', 90: 'noventa',
    }

    if numeral1 > 99 or numeral1 < 0:
        raise ValueError('O número deve estar entre 0 e 99 (inclusive)')

    if numeral1 < 20 or numeral1 % 10 == 0:
        return dicionario_numerico.get(numeral1)

    decimal = numeral1 // 10 * 10
    unidade = numeral1 % 10
    extenso = f'{dicionario_numerico.get(decimal)} e {dicionario_numerico.get(unidade)}'
    return extenso


if __name__ == '__main__':
    print('Insira um número: ')
    numeral = int(input())
    numero_por_extenso = converter_em_texto(numeral)
    print(numero_por_extenso)
