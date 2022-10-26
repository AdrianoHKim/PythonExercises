""" 12. Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos."""


if __name__ == '__main__':
    qtde_alunos = 0

    idades = [17, 18, 13, 10, 9, 15, 18, 15, 13, 10,
              17, 18, 13, 10, 9, 15, 18, 15, 13, 10,
              17, 18, 13, 10, 9, 15, 18, 15, 13, 10]

    alturas = [1.65, 1.56, 1.80, 1.20, 1.50, 1.75, 1.26, 1.30, 1.45, 1.69,
               1.78, 1.58, 1.58, 1.54, 1.60, 1.70, 1.90, 1.52, 1.24, 1.25,
               1.20, 1.54, 1.58, 1.70, 1.85, 1.27, 1.34, 1.28, 1.67, 1.87]

    media_altura = sum(alturas)/len(alturas)

    for i in range(0, len(idades)):
        if idades[i] > 13 and alturas[i] < media_altura:
            qtde_alunos += 1

    print('A quantidade de alunos com mais de 13 anos e uma altura inferior a media(dos alunos) é: ', str(qtde_alunos))
