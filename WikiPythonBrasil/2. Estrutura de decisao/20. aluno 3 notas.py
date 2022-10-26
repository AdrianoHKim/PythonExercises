""" 20. Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""


if __name__ == '__main__':
    n1 = float(input('Digite a primeira nota:'))
    n2 = float(input('Digite a segunda nota:'))
    n3 = float(input('Digite a terceira nota:'))
    med = (n1 + n2 + n3)/3

    if med >= 7 and med != 10:
        print('Média do aluno: ', med, '\nAprovado.')

    elif med < 7:
        print('Média do aluno: ', med, '\nReprovado.')

    else:
        print('Média do aluno: ', med, '\nAprovado com Distinção!')
