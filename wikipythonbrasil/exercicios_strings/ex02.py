""" 2. Nome ao contrário em maiúsculas.
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o
nome do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
"""


if __name__ == '__main__':
    nome = str(input('Digite um nome: '))
    nome2 = nome.upper()[::-1]

    print('Nome ao contrario e com letras maiusculas: ', nome2)
