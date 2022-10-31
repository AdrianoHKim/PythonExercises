""" 13. Desenha moldura. Construa uma função que desenhe um retângulo
usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
Esta função deve receber dois parâmetros, linhas e colunas,
sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
Se valores fora da faixa forem informados,
eles devem ser modificados para valores dentro da faixa de forma elegante.

"""


if __name__ == '__main__':
    def moldura(linha, coluna):
        if linha > 20:
            linha = 20
        if coluna > 20:
            coluna = 20

        print('Resultado:\n')
        a = linha * '-'
        print(f'+{a}+')

        for n in range(coluna):
            n += 1
            b = ' ' * linha
            print(f'|{b}|')

        a = linha * '-'
        print(f'+{a}+')


    linhas = int(input('Digite o numero de linhas ( - ), minimo 1, maximo 20 : '))
    colunas = int(input('Digite o numero de colunas ( | ), minimo 1, maximo 20: '))

    moldura(linhas, colunas)
