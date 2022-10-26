""" 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. """


if __name__ == '__main__':
    i = 1

    while i in range(1, 51):
        print(i, end=' ')
        if i == 50:
            break
        i += 2
