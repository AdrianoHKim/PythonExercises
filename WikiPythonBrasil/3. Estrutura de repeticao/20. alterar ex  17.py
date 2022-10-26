""" 20. Altere o programa de cálculo do fatorial,
permitindo ao usuário calcular o fatorial várias vezes e
limitando o fatorial a números inteiros positivos e menores que 16.
"""


import math

if __name__ == '__main__':
    n = int(0)

    while int(n) < 16 or int(n) > 0:
        n = int(input('Digite um numero positivo e menor que 16: '))
        factorial = 1
        if int(n) > 15 or int(n) < 0:
            print('O numero deve ser maior que 0 e menor que 16! Reinicie o programa')
            break
        for i in range(1, int(n)+1):
            factorial = factorial * i
        print('O fatorial do numero', n, ' é : ', factorial)
        print('Teste:', math.factorial(n))  # teste
