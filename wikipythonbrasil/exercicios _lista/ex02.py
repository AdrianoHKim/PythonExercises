""" Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""


if __name__ == '__main__':
    listaNumeros = []

    print('Informe 10 números')
    for i in range(10):
        listaNumeros.append(input('Numero ' + str(i+1) + ': '))

    listaNumeros.reverse()
    print('Os números informados foram: ', listaNumeros)
