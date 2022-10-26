""" 4. Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’,
 se seu argumento for zero ou negativo.
 """


if __name__ == '__main__':
    def ex4(n):
        if n >= 0:
            print('P')
        elif n < 0:
            print('N')


    num = float(input('Digite um numero: '))
    ex4(num)
