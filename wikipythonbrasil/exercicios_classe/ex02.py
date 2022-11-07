""" 2.Classe Quadrado: Crie uma classe que modele um quadrado:

A: Atributos: Tamanho do lado
B: Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""


class Quadrado:
    def __init__(self, tamlado):
        self.tamlado = tamlado

    def valorlado(self):
        print('Tamanho atual do lado do quadrado: {}'.format(self.tamlado))
        perg1 = input("Deseja alterar o tamanho do lado? [s/n]: ").lower()
        if perg1 == 's':
            perg2 = input('Digite o tamanho do lado: ')
            self.tamlado = perg2

    def retornavalor(self):
        print('Lado do quadrado atual: {}'.format(self.tamlado))

    def calculararea(self):
        result = (int(self.tamlado) * int(self.tamlado))
        print('A area do quadrado é: {}'.format(result))


def main():
    quad = Quadrado(2)

    while True:
        print('----Calculador de área de qudrados----')
        quad.valorlado()
        quad.retornavalor()
        quad.calculararea()
        continuar = input('\nDeseja realizar outra operacao? [s/n]: ').lower()
        if continuar == "n":
            print('Programa finalizado.')
            break


if __name__ == '__main__':
    main()
