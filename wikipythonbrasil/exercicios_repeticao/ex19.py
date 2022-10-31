""" Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

18. Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.

"""


if __name__ == '__main__':
    condition = True
    soma = 0
    numero = []
    conjunto = int(input('Digite a quantidade de numeros no conjunto: '))

    while condition:
        num = int(input('Digite um numero (0 a 1000): '))
        if num != 0:
            soma += num
            numero.append(num)
        if len(numero) == conjunto:
            break
        if num < 0 or num > 1000:
            print('Numero invalido, digite apenas numeros entre 0 e 1000!')
            print('Reinicie o programa!')
            exit()

    print('A soma dos numeros do conjunto é: ', soma)
    print('O menor valor no conjunto é: ', min(numero))
    print('O maior valor no conjunto é: ', max(numero))
