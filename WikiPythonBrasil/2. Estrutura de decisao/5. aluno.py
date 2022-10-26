""" 5.Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""


if __name__ == '__main__':
    n1 = float(input('Digite a primeira nota:'))
    n2 = float(input('Digite a segunda nota:'))
    med = (n1+n2)/2

    if med >= 7 and med != 10:
        print('Média do aluno: ', med, '\nAprovado.')

    elif med < 7:
        print('Média do aluno: ', med, '\nReprovado.')

    else:
        print('Média do aluno: ', med, '\nAprovado com Distinção!')
