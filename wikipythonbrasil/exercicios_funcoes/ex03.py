""" 3. Faça um programa, com uma função que necessite de três argumentos,
 e que forneça a soma desses três argumentos.
 """


if __name__ == '__main__':
    def ex3(n):
        soma = []
        for a in range(n):
            soma.append(int(input('Digite um numero: ')))
        print(f'A soma dos tres numeros é: {sum(soma)}')


    ex3(3)
