""" Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""


if __name__ == '__main__':
    listaNumeros = []

    print('Informe 5 números')

    for i in range(5):
        listaNumeros.append(input('Numero ' + str(i+1) + ': '))

    print('Os números informados foram: ', listaNumeros)
