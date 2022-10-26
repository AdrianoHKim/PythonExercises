""" 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante. """


if __name__ == '__main__':
    letra = str.upper(input('Digite  a letra: '))
    lista = str(list['A', 'E', 'I', 'O', 'U'])

    if letra in lista:
        print('A letra é uma vogal.')

    else:
        print('A letra é uma consoante.')
