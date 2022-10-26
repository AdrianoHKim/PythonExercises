""" 14. Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""


if __name__ == '__main__':
    pares = 0
    for x in range(10):
        n = int(input("Digite um número:"))
        if n % 2 == 0:
            pares = pares + 1

    print(pares, "números par(es)")
    print((10 - pares), "números ímpar(es)")
