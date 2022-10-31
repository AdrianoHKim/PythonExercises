""" 1.Faça um Programa que peça dois números e imprima o maior deles. """


if __name__ == '__main__':
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if n1 > n2:
        print('O maior número é: ', n1)

    elif n1 == n2:
        print('Os dois numeros são iguais!')

    else:
        print('O maior número é: ', n2)
