""" 14. Faça um programa que lê as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""


if __name__ == '__main__':
    n1 = float(input('Digite a primeira nota parcial:'))
    n2 = float(input('Digite a segunda nota parcial:'))
    med = (n1 + n2) / 2

    if med <= 3.999:
        print('==Resultado==')
        print('Parcial 1:', n1, '| Parcial 2:', n2, '| Média:', med)
        print('Conceito: E')
        print('Status: Reprovado')

    elif med <= 5.999:
        print('==Resultado==')
        print('Parcial 1:', n1, '| Parcial 2:', n2, '| Média:', med)
        print('Conceito: D')
        print('Status: Reprovado')

    elif med <= 7.499:
        print('==Resultado==')
        print('Parcial 1:', n1, '| Parcial 2:', n2, '| Média:', med)
        print('Conceito: C')
        print('Status: Aprovado')

    elif med <= 8.999:
        print('==Resultado==')
        print('Parcial 1:', n1, '| Parcial 2:', n2, '| Média:', med)
        print('Conceito: B')
        print('Status: Aprovado')

    else:
        print('==Resultado==')
        print('Parcial 1:', n1, '| Parcial 2:', n2, '| Média:', med)
        print('Conceito: A')
        print('Status: Aprovado')
