""" Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""


if __name__ == '__main__':
    listaNumeros = []

    print('Informe 4 números')

    for i in range(4):
        listaNumeros.append(int(input('Digite um numero: ')))

    print('Media dos numeros informados: ', sum(listaNumeros)/4)
