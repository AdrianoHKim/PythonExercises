""" 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""


if __name__ == '__main__':
    p1 = str.upper(input('Telefonou para a vítima? (S/N): '))
    p2 = str.upper(input('Esteve no local do crime? (S/N): '))
    p3 = str.upper(input('Mora perto da vítima? (S/N): '))
    p4 = str.upper(input('Devia para a vítima? (S/N): '))
    p5 = str.upper(input('Já trabalhou com a vítima? (S/N): '))

    pontos = 0

    if p1 == 'S':
        pontos = pontos + 1
    if p2 == 'S':
        pontos = pontos + 1
    if p3 == 'S':
        pontos = pontos + 1
    if p4 == 'S':
        pontos = pontos + 1
    if p5 == 'S':
        pontos = pontos + 1

    if pontos == 2:
        print('Classificação: Suspeita')

    if pontos == 3 or pontos == 4:
        print('Classificação: Cúmplice')

    if pontos == 5:
        print('Classificação: Assassino!')

    if pontos < 2:
        print('Classificação: Inocente')
