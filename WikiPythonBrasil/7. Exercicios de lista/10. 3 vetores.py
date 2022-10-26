""" 10. Faça um Programa que leia dois vetores com 10 elementos cada.
 Gere um terceiro vetor de 20 elementos, cujos valores deverão
 ser compostos pelos elementos intercalados dos dois outros vetores.
"""


if __name__ == '__main__':
    lista1, lista2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    lista3 = []

    for elemento in range(0, 10):
        lista3.append(lista1[elemento])
        lista3.append(lista2[elemento])

    print(lista3)
