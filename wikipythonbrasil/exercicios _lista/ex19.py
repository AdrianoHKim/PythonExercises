""" 19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a
um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final
o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a
entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual
de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado
pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos."""

import numpy

opcoes = ['0', '1', '2', '3', '4', '5', '6']
votos = []
duplicados = set()


def cont_func(cont):
    contagem = votos.count(cont)
    return contagem


if __name__ == '__main__':
    while True:
        num = str(input('Qual o melhor Sistema Operacional para uso em servidores?\n1- Windows Server\n2- Unix\n'
                        '3- Linux\n4- Netware\n5- Mac OS\n6- Outro\nResposta: '))

        if num not in opcoes:
            print('Informe um valor entre 1 e 6 ou 0 para sair!')
        if num == '0':
            print('Programa encerrado!\n')
            break
        if num == '1':
            votos.append('Windows Server')
        if num == '2':
            votos.append('Unix')
        if num == '3':
            votos.append('Linux')
        if num == '4':
            votos.append('Netware')
        if num == '5':
            votos.append('Mac OS')
        if num == '6':
            votos.append('Outro')

    print('{:<8} {:<12} {:<4}'.format('Sistema Operacional', 'Votos', '%'))
    print('{:<8} {:<12} {:<4}'.format('-------------------', '-----', '---'))

    for n in votos:
        if n not in duplicados:
            print('{:<21} {:<10} {:<1} {:<10}'.format(n, cont_func(n),
                  "{:.0f}".format(((cont_func(n)) / len(votos)) * 100), '%'))
            duplicados.add(n)

    print('{:<12} {:<12}'.format('-------------------', '-----'))
    print('{:<21} {:<12}'.format('Total', len(votos), '---'))

    asd = numpy.array(votos)

    print(f'O Sistema Operacional mais votado foi o {max(votos, key=votos.count)}, '
          f'com {cont_func(max(votos, key=votos.count))} votos, correspondendo a'
          f' {"{:.0f}".format((cont_func(max(votos, key=votos.count))) / len(votos) * 100)}% dos votos.')
