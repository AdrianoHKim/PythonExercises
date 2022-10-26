""" 1. Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Ball:
    def __init__(self, color='Unknown', circumference=0, material='Unknown'):
        self.color = color
        self.circunf = circumference
        self.material = material

    def trocacor(self):
        troca = input('Deseja mudar a cor atual? [s/n]: ').lower()

        if troca == 's':
            nova_cor = input("\nDigite a cor desejada: ")
            self.color = nova_cor
            print('Cor atual alterada para {}.'.format(self.color))
        else:
            print("A cor nao foi alterada")

    def mostracor(self):
        print("\nA cor atual é {}.".format(self.color))


def main():
    ball1 = Ball("Incolor", 2, "Glass")

    while True:
        ball1.mostracor()
        ball1.trocacor()

        continuar = input("Deseja alterar a cor novamente? [s/n]").lower()
        if continuar == "n":
            ball1.mostracor()
            print('Programa Finalizado')
            break


if __name__ == '__main__':
    main()
