""" 15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""


if __name__ == '__main__':
    n = int(input('Inserir um numero para gerar a sequência de Fibonnaci :'))

    u_1 = 1
    u_2 = 1
    count = 0

    lista = [1, 1]

    for vic in range(1, n):
        count = u_1 + u_2
        u_1 = count
        u_2 = (count - u_2)
        lista.append(count)

    print(lista)
