""" 10. Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor."""


def quadrado(n):
    return [x ** 2 for x in n]


if __name__ == '__main__':
    lista = []

    for i in range(10):
        numero = float(input('Digite um numero: '))
        lista.append(numero)

    print('A soma dos quadrados dos elementos da lista é: ', sum(quadrado(lista)))
