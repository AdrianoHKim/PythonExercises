""" 8. Faça um programa que leia 5 números e informe a soma e a média dos números """


if __name__ == '__main__':
    num = [int(input('Informe um número: ')) for x in range(5)]

    print('A soma dos numeros é: ', sum(num))
    print('A media dos numeros é: ', sum(num) / 5)
