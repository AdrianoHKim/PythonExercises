""" Faça um Programa que leia um vetor de 10 caracteres,
e diga quantas consoantes foram lidas. Imprima as consoantes."""


if __name__ == '__main__':
    listaletras = []
    consoantes = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                  'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    letra = str(input('Digite uma palavra: ')).lower()

    for i in letra:
        if i in consoantes:
            listaletras.append(i)

    print(f'Foram lidas {len(listaletras)} consoantes :', listaletras)
