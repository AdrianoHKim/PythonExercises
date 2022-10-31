""" 11.Data com mês por extenso.
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
 formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso
 a data seja inválida."""


if __name__ == '__main__':
    listames = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho',
                'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    mes31 = [1, 3, 5, 7, 8, 10, 12]
    mes30 = [4, 6, 9, 11]


    def conversao(data):
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])

        valida = False

        if mes in mes31:
            if dia <= 31:
                valida = True

        if mes in mes30:
            if dia <= 30:
                valida = True

        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                if dia <= 29:
                    valida = True
            elif dia <= 28:
                valida = True

        if valida:
            print(f'Data convertida: {dia} de {listames[mes - 1]} de {ano}')

        else:
            raise Exception('NULL - Data invalida!')


    pergunta = input('Digite a data neste formato (DD/MM/AAAA): ')

    conversao(pergunta)
