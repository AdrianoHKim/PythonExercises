""" 3. Faça um Programa que verifique se uma letra digitada
 é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""


if __name__ == '__main__':
    sexo = str.upper(input('Digite o sexo: '))

    if sexo == 'F':
        print('F - Feminino')

    elif sexo == 'M':
        print('M - Masculino')

    else:
        print('Sexo Inválido')
