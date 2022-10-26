""" 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
 descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
 faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""


if __name__ == '__main__':
    valor = float(input('Digite o valor ganho por hora trabalhada: '))
    hora = float(input('Digite quantas horas foram trabalhadas no mês: '))
    sal = valor * hora
    ir = sal * 0.11
    inss = sal * 0.08
    sindi = sal * 0.05

    print('+Salário Bruto: R$', '{:.2f}'.format(sal))
    print('- IR (11%) : R$', '{:.2f}'.format(ir))
    print('- INSS (8%) : R$', '{:.2f}'.format(inss))
    print('- Sindicato ( 5%) : R$', '{:.2f}'.format(sindi))
    print('= Salário Liquido : R$', '{:.2f}'.format(sal - (ir + inss + sindi)))
