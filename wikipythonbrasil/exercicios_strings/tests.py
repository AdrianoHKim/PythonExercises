from itertools import permutations


def validarcubo(a):
    if sum(a[:3]) == sum(a[3:6]) == sum(a[6:9]) == (a[0] + a[4] + a[8]) == (a[2] + a[4] + a[6]):
        print(a)
        return 1
    else:
        return 0


def gerarcubos(tab):
    cont = 0
    validos = 0
    for i in permutations(tab, 9):
        cont += 1
        validos += validarcubo(i)
    print(f'Total de simulacoes: {cont}\nTotal de quadrados magicos: {validos}')


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

gerarcubos(lista)
