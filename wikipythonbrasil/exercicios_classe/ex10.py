""" 10. Classe Bomba de Combustível: Faça um programa completo utilizando classes e
métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e
mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de
 combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível
restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a
quantidade de combustível total na bomba."""


class BombaCombustivel:
    def __init__(self, tipocombustivel, valorlitro: float, quantidadecombustivel):
        self.tipocombustivel = tipocombustivel
        self.valorlitro = valorlitro
        self.quantidadecombustivel = quantidadecombustivel

    def alterarcombustivel(self):
        print('Combustivel atual: {}'.format(self.tipocombustivel))
        altcomb = input("Deseja alterar o combustivel? [s/n]").lower()
        if altcomb == 's':
            novocomb = input('Digite o tipo de combustivel: ')
            self.tipocombustivel = novocomb
            print('Combustivel atual alterado para {}.'.format(self.tipocombustivel))

    def alterarvalor(self):
        print('Valor atual por litro: R$ {}'.format(self.valorlitro))
        altval = input("Deseja alterar o valor? [s/n]: ").lower()
        if altval == 's':
            novoval = float(input('Digite o valor por litro: '))
            self.valorlitro = novoval
            print('Preco por litro alterado para R$ {}.'.format(self.valorlitro))

    def abastecerporvalor(self):
        perg1 = input("Deseja abastecer por valor? [s/n]: ").lower()
        if perg1 == 's':
            perg2 = float(input('Digite o valor: '))
            if perg2/self.valorlitro > self.quantidadecombustivel:
                print('Quantidade de litros insuficiente na bomba, litros restantes: {}'
                      '\nDiminua o valor a ser abastecido.'.format(self.quantidadecombustivel))
            else:
                qtdelitro = perg2/self.valorlitro
                estoque = self.quantidadecombustivel-qtdelitro
                print('-------Recibo-------\nTipo de combustivel: {}\nValor por litro: {}\n'
                      'Valor pago R$: {}\n'
                      'Quantidade de litros abastecido: {}'
                      '\nQuantidade restante de litros na bomba: {}'
                      .format(self.tipocombustivel, self.valorlitro, perg2, qtdelitro, estoque))
                continuar = input('Deseja alterar algum item ou abastecer novamente? [s/n]: ').lower()
                if continuar == 's':
                    pass
                else:
                    print('Programa finalizado!')
                    exit()

    def abastecerporlitro(self):
        perg2 = float(input('Digite a quantidade de litros: '))
        if perg2 > self.quantidadecombustivel:
            print('Quantidade de litros insuficiente na bomba, litros restantes: {}'
                  '\nDiminua a quantidade de litros a ser abastecido.'
                  .format(self.quantidadecombustivel))
        else:
            estoque = self.quantidadecombustivel-perg2
            valorpago = perg2 * self.valorlitro
            print('-------Recibo-------\nTipo de combustivel: {}\nValor por litro: {}'
                  '\nValor pago R$: {}\n'
                  'Quantidade de litros abastecido: {}'
                  '\nQuantidade restante de litros na bomba: {}'
                  .format(self.tipocombustivel, self.valorlitro, valorpago, perg2, estoque))


def main():
    bomba1 = BombaCombustivel('alcool', 1.76, 100)

    while True:
        bomba1.alterarcombustivel()
        bomba1.alterarvalor()
        bomba1.abastecerporvalor()
        continuar = input('Deseja abastecer por litro? [s/n]: ').lower()
        if continuar == "n":
            print('Programa finalizado.')
            break
        bomba1.abastecerporlitro()
        continuar2 = input('Deseja alterar algum item ou abastecer novamente? [s/n]: ').lower()
        if continuar2 == "n":
            print('Programa finalizado.')
            break


if __name__ == '__main__':
    main()
