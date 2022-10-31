""" 6. Data por extenso. Faça um programa que solicite a
data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.

"""


if __name__ == '__main__':
    meses = ['Janeiro',
             'Fevereiro',
             'Março',
             'Abril',
             'Maio',
             'Junho',
             'Julho',
             'Agosto',
             'Setembro',
             'Outubro',
             'Novembro',
             'Dezembro']

    data = input('Digite uma data no formato (dd/mm/aaaa): ')


    print(data.split('/')[0],
          'de',
          meses[(int(data.split('/')[1]) - 1)],
          'de',
          data.split('/')[2] + '.')
