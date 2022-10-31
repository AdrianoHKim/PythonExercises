""" 6.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""


if __name__ == '__main__':
    raio = float(input('Digite o tamanho do raio do círculo: '))

    # Obs.: Valor de π(Pi): 3.14 arredondado
    # Fórmula da area do circulo: π * (raio ** 2)
    # '**' fórmula de exponenciação

    print('A área do circulo é:', 3.14 * (raio ** 2))
