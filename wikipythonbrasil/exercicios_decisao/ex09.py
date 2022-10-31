""" 9. Faça um Programa que leia três números e mostre-os em ordem decrescente. """


if __name__ == '__main__':
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))

    lista = [n1, n2, n3]
    lista2 = sorted(lista, reverse=True)

    print('Os números em ordem decrescente: ', lista2)
