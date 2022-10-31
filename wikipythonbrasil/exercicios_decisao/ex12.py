""" 12. Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Sindicato (3%)                  : R$   33,00
        Total de descontos              : R$  198,00
        Salário Liquido                 : R$  902,00

"""


if __name__ == '__main__':
    valor = float(input('Digite o valor da hora trabalhada: '))
    hr = float(input('Digite a quantidade de horas trabalhadas: '))
    salb = valor * hr
    inss = salb * 0.1
    fgts = salb * 0.11
    sindicato = salb * 0.03
    mony = '{:.2f}'.format

    if salb <= 900:
        print('Salário Bruto: (', valor, '*', hr, ') : R$', mony(salb))
        print('(-) IR (Isento)')
        print('(-) INSS ( 10%): R$ ', mony(inss))
        print('FGTS (11%): R$ ', mony(fgts))
        print('Sindicato (3%): R$ ', mony(sindicato))
        print('Total de descontos: R$ ', mony(inss + fgts + sindicato))
        print('Salário Liquido:', mony(salb - (inss + fgts + sindicato)))

    elif salb <= 1500:
        ir = salb * 0.05
        print('Salário Bruto: (', valor, '*', hr, ') : R$', mony(salb))
        print('(-) IR (5%): R$ ', mony(ir))
        print('(-) INSS ( 10%): R$ ', mony(inss))
        print('FGTS (11%): R$ ', mony(fgts))
        print('Sindicato (3%): R$ ', mony(sindicato))
        print('Total de descontos: R$ ', mony(inss + fgts + sindicato + ir))
        print('Salário Liquido:', mony(salb - (inss + fgts + sindicato + ir)))

    elif salb <= 2500:
        ir = salb * 0.1
        print('Salário Bruto: (', valor, '*', hr, ') : R$', mony(salb))
        print('(-) IR (10%): R$ ', mony(ir))
        print('(-) INSS ( 10%): R$ ', mony(inss))
        print('FGTS (11%): R$ ', mony(fgts))
        print('Sindicato (3%): R$ ', mony(sindicato))
        print('Total de descontos: R$ ', mony(inss + fgts + sindicato + ir))
        print('Salário Liquido:', mony(salb - (inss + fgts + sindicato + ir)))

    else:
        ir = salb * 0.2
        print('Salário Bruto: (', valor, '*', hr, ') : R$', mony(salb))
        print('(-) IR (20%): R$ ', mony(ir))
        print('(-) INSS ( 10%): R$ ', mony(inss))
        print('FGTS (11%): R$ ', mony(fgts))
        print('Sindicato (3%): R$ ', mony(sindicato))
        print('Total de descontos: R$ ', mony(inss + fgts + sindicato + ir))
        print('Salário Liquido:', mony(salb - (inss + fgts + sindicato + ir)))
