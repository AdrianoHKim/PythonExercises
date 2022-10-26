""" 11.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador
e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 281,00 e R$ 700,00(incluindo) : aumento de 15%
salários entre R$ 701,00 e R$ 1500,00(incluindo) : aumento de 10%
salários de R$ 1501,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""


if __name__ == '__main__':
    sal = float(input('Digite o valor do sálario:'))
    mony = '{:.2f}'.format


    if sal <= 280:
        print('Sálario: R$', mony(sal))
        print('Aumento de 20%')
        print('Valor do aumento: R$', mony(sal * 0.2))
        print('Sálario reajustado: R$', mony(sal * 1.2))

    elif sal <= 281 <= 700:
        print('Sálario: R$', mony(sal))
        print('Aumento de 15%')
        print('Valor do aumento: R$', mony(sal * 0.15))
        print('Sálario reajustado: R$', mony(sal * 1.15))

    elif sal <= 701 <= 1500:
        print('Sálario: R$', mony(sal))
        print('Aumento de 10%')
        print('Valor do aumento: R$', mony(sal * 0.1))
        print('Sálario reajustado: R$', mony(sal * 1.1))

    else:
        print('Sálario: R$', mony(sal))
        print('Aumento de 5%')
        print('Valor do aumento: R$', mony(sal * 0.05))
        print('Sálario reajustado: R$', mony(sal * 1.05))
