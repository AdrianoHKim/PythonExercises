""" 7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
# desta área para o usuário.
"""


if __name__ == '__main__':
    lado = float(input('Digite o tamanho do lado do quadrado: '))

    # Obs.: Fórmula da área do quadrado = lado * lado

    print('O dobro da área deste quadrado é: ', format((lado * lado) * 2, 'n'))
