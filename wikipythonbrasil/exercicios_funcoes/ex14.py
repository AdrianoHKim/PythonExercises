""" 14. Elabore uma função que identifica e mostra na tela
todos os quadrados mágicos com as características acima.
Dica: produza todas as combinações possíveis e verifique a
soma quando completar cada quadrado. Usar um vetor de 1 a 9
parece ser mais simples que usar uma matriz 3x3.

8  3  4
1  5  9
6  7  2

"""


if __name__ == '__main__':
    from itertools import permutations


    def validarquadrado(a):
        if sum(a[0:3]) == sum(a[3:6]) == sum(a[6:9]) == sum(a[::4]) == sum(a[2:8:2])\
                == sum(a[::3]) == sum(a[1::3]) == sum(a[2::3]):
            print(f'+---------+\n|{a[0]}   {a[1]}   {a[2]}|\n|{a[3]}   {a[4]}  '
                  f' {a[5]}|\n|{a[6]}   {a[7]}   {a[8]}|\n+---------+\n')
            return 1
        else:
            return 0


    def gerarquadrado(tab):
        cont = 0
        validos = 0
        for i in permutations(tab, 9):
            cont += 1
            validos += validarquadrado(i)
        print(f'Total de simulacoes: {cont}\nTotal de quadrados magicos: {validos}')


    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    gerarquadrado(lista)
