""" 23. Faça um programa que mostre todos os primos entre 1 e N
sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para
encontrar os números primos. Serão avaliados o funcionamento,
o estilo e o número de testes (divisões) executados.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""


if __name__ == '__main__':
    num = int(input('Digite um numero: '))
    numero = 2
    cont = 0  # contagem de operacoes
    p = 0  # contagem de numeros primos

    print("Primos: ")

    for div in range(1, num):
        i = numero - 1
        while i > 1:
            if numero % i == 0:
                break
            i -= 1
            cont += 1
        else:
            print(numero, end='|')
            p += 1
        numero += 1

    print("\n\nForam encontrados %d números primos." % p)
    print("Foram necessárias %d comparações." % cont)
