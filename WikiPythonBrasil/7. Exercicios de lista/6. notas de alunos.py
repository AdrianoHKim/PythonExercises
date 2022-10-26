""" 6. Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0."""


if __name__ == '__main__':
    medias = []
    contador = 0

    for i in range(10):
        n1 = int(input('Digite a primeira nota: '))
        n2 = int(input('Digite a segunda nota: '))
        n3 = int(input('Digite a terceira nota: '))
        n4 = int(input('Digite a quarta nota: '))
        media = (n1 + n2 + n3 + n4)/4
        medias.append(media)
        print('Notas cadastradas')

    for x in medias:
        if x > 7:
            contador += 1

    print('Numero de alunos com média maior ou igual a 7: ', contador)
