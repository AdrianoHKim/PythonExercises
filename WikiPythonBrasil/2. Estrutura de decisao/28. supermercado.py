""" 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá
ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário
e gere um cupom fiscal, contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
 """


if __name__ == '__main__':
    tipo = int(input('Digite o tipo de carne:\n1 - Filé Duplo\n2 - Alcatra\n3 - Picanha\nTipo: '))
    quantidade = int(input('Digite a quantidade comprada em kg: '))
    resposta = int(input('A compra será realizada com cartão Tabajara? 1 = SIM | 2 = NAO: '))
    preco = None
    nome = None

    if tipo == 1:
        nome = 'Filé Duplo'
        if quantidade <= 5:
            preco = quantidade * 4.90
        else:
            preco = quantidade * 5.80

    if tipo == 2:
        nome = 'Alcatra'
        if quantidade <= 5:
            preco = quantidade * 5.90
        else:
            preco = quantidade * 6.80

    if tipo == 3:
        nome = 'Picanha'
        if quantidade <= 5:
            preco = quantidade * 6.90
        else:
            preco = quantidade * 7.80

    if resposta == 1:
        r = 'SIM'
        desconto = (preco * 0.05)
        total = preco - desconto

    else:
        r = 'NÃO'
        desconto = 0
        total = preco

    print('\n=====CUPOM FISCAL=====')
    print('* Tipo de Carne: ', nome)
    print('* Quantidade: ', quantidade, 'kg')
    print('* Preço: R$', preco)
    print('* Cartao Tabajara: ', r)
    print('* Valor do desconto: R$', desconto)
    print('* Total a pagar: R$', total)
