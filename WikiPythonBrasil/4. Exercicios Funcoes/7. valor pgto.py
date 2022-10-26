"""7. Faça um programa que use a função valorPagamento para determinar o valor a ser
pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor
da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá
voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor
igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o
relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar
o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso."""


if __name__ == '__main__':
    relatorio = []

    while True:
        valor = float(input('Digite o valor da prestacao: '))
        if valor == 0:
            print(f'Quantidade de prestacoes pagas: {len(relatorio)}')
            print(f'Valor total pago: R$ {"{:.2f}".format(sum(relatorio))}\nPrograma encerrado!')
            exit()
        dia = int(input('Digite quantos dias de atraso: '))


        def valorpagamento(valor1, dias1):
            valorcommulta = valor * 1.03
            formula = float(valorcommulta + (valorcommulta * (dias1 * 0.01)))
            print(f'Valor a ser pago: R$ {"{:.2f}".format(formula)}')
            if valor1 != 0:
                relatorio.append(formula)

        valorpagamento(valor, dia)
