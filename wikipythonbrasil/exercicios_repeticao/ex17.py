""" 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120"
"""

import math


if __name__ == '__main__':
    n = int(input('Digite um numero: '))
    factorial = 1

    if int(n) >= 1:
        for i in range(1, int(n)+1):
            factorial = factorial * i
        print('O fatorial do numero', n, ' é : ', factorial)
        print(math.factorial(n))  # teste
