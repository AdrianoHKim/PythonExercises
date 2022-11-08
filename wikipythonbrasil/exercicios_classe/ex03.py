""" 3. Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias
para o local."""


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudarlados(self):
        self.comprimento = input("Informe o comprimento da area em metros: ")

        self.largura = input("Informe a largura da area em metros: ")

    def retornalados(self):
        print('\nDimensoes da area:\nComprimento: {} mts.\nLargura: {} mts.'.format(self.comprimento, self.largura))

    def calculaarea(self):
        area = int(self.comprimento) * int(self.largura)
        print('Serao necessarios {} metros quadrados de pisos para area.'.format(area))

    def calculaperimetro(self):
        perimetro = (int(self.comprimento) * 2) + (int(self.largura) * 2)
        print('Serao necessarios {} metros lineares de pisos para os rodapes'.format(perimetro))


def main():
    area1 = Retangulo(2, 2)

    while True:
        area1.mudarlados()
        area1.retornalados()
        area1.calculaarea()
        area1.calculaperimetro()
        continuar = input('\nDeseja realizar outra operacao? [s/n]: ').lower()
        if continuar == "n":
            print('Programa finalizado.')
            break


if __name__ == '__main__':
    main()
