""" 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima
a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""


if __name__ == '__main__':
    num = input('Digite um numero maior que 0 e menor que 1000: ')
    numeroStr = str(num)
    qtNumero = len(numeroStr)

    if qtNumero == 3:
        cent = numeroStr[0]
        dez = numeroStr[1]
        uni = numeroStr[2]
        c = 'centenas'
        d = 'dezenas'
        u = 'unidades'
        if cent == '1':
            c = 'centena'
        if dez == '1':
            d = 'dezena'
        if uni == '1':
            u = 'unidade'
        print(num, '=', cent, c, ',', dez, d, 'e', uni, u)

    if qtNumero == 2:
        dez = numeroStr[0]
        uni = numeroStr[1]
        d = 'dezenas'
        u = 'unidades'
        if dez == '1':
            d = 'dezena'
        if uni == '1':
            u = 'unidade'
        print(num, '=', dez, d, 'e', uni, u)

    if qtNumero == 1:
        uni = numeroStr[0]
        u = 'unidades'
        if uni == '1':
            u = 'unidade'
        print(num, '=', uni, u)
