""" 5. Nome na vertical em escada invertida.
Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F

"""


if __name__ == '__main__':
    nome = str.upper(input('Digite um nome: '))

    tamanho_nome = len(nome)
    contador = tamanho_nome

    while contador > 0:
        print(nome[0:contador])
        contador = contador - 1
