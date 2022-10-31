""" 22. Altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
"""


if __name__ == '__main__':
    numero = int(input('Digite um numero: '))
    lista = []
    divisores = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            lista.append(divisor)

    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
                break

    if divisores > 1 or numero == 1 or numero == 0:
        lista.append(numero)
        print('O numero não é primo, é divisivel por: ', lista)

    else:
        lista.append(numero)
        print('O numero é primo, divisivel apenas por: ', lista)
