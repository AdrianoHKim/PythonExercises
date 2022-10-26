""" 10. Faça um programa que receba dois números inteiros e gere os números inteiros
 que estão no intervalo compreendido por eles.
 """


if __name__ == '__main__':
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))

    for i in range(n1 + 1, n2):
        print(i, end=' ')
