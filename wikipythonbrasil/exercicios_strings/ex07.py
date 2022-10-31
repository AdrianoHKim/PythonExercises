""" 7. Conta espaços e vogais.
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
conte:

a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.

"""


if __name__ == '__main__':
    frase = input('Digite uma frase: ')

    a = frase.count('a')
    e = frase.count('e')
    i = frase.count('i')
    o = frase.count('o')
    u = frase.count('u')
    branco = frase.count(' ')

    print('Quantidade de espacos em branco na frase: ', branco)

    print('Quantidade de vogais: \nA: %d\nE: %d\nI: %d\nO: %d\nU: %d' % (a, e, i, o, u))
