""" 14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
 As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma
classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada
 como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
 Caso contrário, ele será classificado como "Inocente"."""


if __name__ == '__main__':
    resp = []

    p1 = input('Telefonou para a vítima? S/N: ').upper()
    if p1 == 'S':
        resp.append(p1)

    p2 = input('Esteve no local do crime? S/N: ').upper()
    if p2 == 'S':
        resp.append(p2)

    p3 = input('Mora perto da vítima? S/N: ').upper()
    if p3 == 'S':
        resp.append(p3)

    p4 = input('Devia para a vítima? S/N: ').upper()
    if p4 == 'S':
        resp.append(p4)

    p5 = input('Já trabalhou com a vítima?  S/N: ').upper
    if p5 == 'S':
        resp.append(p5)

    if len(resp) == 2:
        print('Essa pessoa é considerada: Suspeita')

    if len(resp) == 3 or len(resp) == 4:
        print('Essa pessoa é considerada: Cumplice')

    if len(resp) == 5:
        print('Essa pessoa é considerada: Assassino')

    if len(resp) == 0 or len(resp) == 1:
        print('Essa pessoa é considerada: Inocente')
