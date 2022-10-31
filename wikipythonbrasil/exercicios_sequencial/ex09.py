""" 9.Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
Fórmula C = 5 * ((F-32) / 9). """


if __name__ == '__main__':
    fah = float(input('Digite a temperatura em Fahrenheit: '))

    print('A temperatura em Celsius é: ', 5 * ((fah - 32)/9))
