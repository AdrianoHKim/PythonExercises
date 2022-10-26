""" 1.Tamanho de strings.
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
"""


if __name__ == '__main__':
    print('Compara duas strings')

    str1 = str(input('Digite a primeira string: '))
    str2 = str(input('Digite a segunda string: '))

    print('Tamanho de "', str1, '" :', len(str1), 'caracteres')
    print('Tamanho de "', str2, '" :', len(str2), 'caracteres')

    if len(str1) != len(str2):
        print('As duas strings são de tamanhos diferentes.')
    else:
        print('As duas strings tem tamanhos iguais.')

    if str1 != str2:
        print('As duas strings possuem conteúdos diferentes.')
    else:
        print('As duas strings possuem conteúdos iguais.')
