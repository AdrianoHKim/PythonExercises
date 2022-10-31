""" 9.Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 127 -> 721."""


if __name__ == '__main__':
    def reverso(num):
        num = str(num)
        print('O reverso do numero é:', num[::-1])


    numero = int(input('Digite um numero inteiro: '))

    reverso(numero)
