""" 10.Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.
Fórmula : (C × (9/5)) + 32 = F
"""

if __name__ == '__main__':
    cel = float(input('Digite a temperatura em Celsius:'))

    print('A temperatura em Fahrenheit é: ', (cel * (9/5)) + 32)
