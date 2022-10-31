""" 5. Faça um programa com uma função chamada somaImposto.
 A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa
 em porcentagem; E custo, que é o custo de um item antes do imposto.
 A função “altera” o valor de custo para incluir o imposto sobre vendas.
 """


if __name__ == '__main__':
    def somaimposto(custo, taxaimposto):
        print('O valor final com imposto sera: R${:.2f}'.format(custo * ((taxaimposto/100) + 1)))


    a = float(input('Digite o valor de custo bruto do produto: '))
    b = float(input('Digite o valor do imposto, em porcentagem: '))

    somaimposto(a, b)
