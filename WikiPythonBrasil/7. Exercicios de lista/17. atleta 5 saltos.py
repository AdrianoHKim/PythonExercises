""" 17. Em uma competição de salto em distância cada atleta
tem direito a cinco saltos. O resultado do atleta será determinado
pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias
alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos
e a média dos saltos. O programa deve ser encerrado quando não for informado
 o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""


if __name__ == '__main__':
    lista = []
    saltos = ['Primeiro salto', 'Segundo salto', 'Terceiro salto', 'Quarto salto', 'Quinto salto']

    while True:
        nome = input('Digite o nome do atleta: ')
        if nome == '':
            print('Programa encerrado! Reinicie o programa e informe um nome.')
            break
        for i in range(5):
            lista.append(float(input('Digite a distancia do salto: ')))

        media = sum(lista)/5

        print('Atleta: ', nome, '\n')

        for x in range(5):
            print(f'{saltos[x]}: {lista[x]} m ')
        print('')

        print('Resultado final:')
        print('Atleta: ', nome)
        print(f'Saltos: {lista[0]} - {lista[1]} - {lista[2]} - {lista[3]} - {lista[4]}')
        print(f'Media dos saltos: {media} m \n')
