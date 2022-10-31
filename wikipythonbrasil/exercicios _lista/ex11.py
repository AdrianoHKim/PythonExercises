""" 11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""


if __name__ == '__main__':
    lista1, lista2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    lista3 = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    lista4 = []

    for elemento in range(0, 10):
        lista4.append(lista1[elemento])
        lista4.append(lista2[elemento])
        lista4.append(lista3[elemento])

    print(lista4)
