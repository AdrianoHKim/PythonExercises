""" 18. Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
"""


if __name__ == '__main__':
    condition = True
    soma = 0
    numero = []
    conjunto = int(input('Digite a quantidade de numeros no conjunto: '))

    while condition:
        num = int(input('Digite um numero: '))
        if num != 0:
            soma += num
            numero.append(num)
        if len(numero) == conjunto:
            break

    print('A soma dos numeros do conjunto é: ', soma)
    print('O menor valor no conjunto é: ', min(numero))
    print('O maior valor no conjunto é: ', max(numero))
