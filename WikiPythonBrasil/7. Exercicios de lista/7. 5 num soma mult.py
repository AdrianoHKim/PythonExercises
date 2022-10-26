""" 7. Faça um Programa que leia um vetor de 5 números inteiros,
 mostre a soma, a multiplicação e os números."""


if __name__ == '__main__':
    lista = []


    def soma_da_lista(n):
        total = 0
        for val in n:
            total += val
        return total


    def mult_da_lista(m):
        total = 1
        for val in m:
            total *= val
        return total


    for x in range(5):
        numero = int(input('Digite um numero: '))
        lista.append(numero)

    print('A soma dos numeros da lista é: ', soma_da_lista(lista))
    print('A multiplicacao dos numeros da lista é: ', mult_da_lista(lista))
    print('Lista de numeros: ', lista)


""" outro ex.:

import math
lista = []


for x in range(5):
    numero = int(input('Digite um numero: '))
    lista.append(numero)


print('Lista de numeros: ', lista)
print('Soma da lista:', sum(lista))
print('A multipicação dos elementos da lista é:', math.prod(lista))
"""
