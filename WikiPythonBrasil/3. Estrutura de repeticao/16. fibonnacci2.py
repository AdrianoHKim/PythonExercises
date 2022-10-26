""" 16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""


if __name__ == '__main__':
    n = 1
    u_1 = 1
    u_2 = 1
    count = 0

    lista = [1, 1]

    for vic in range(n, 14):
        count = u_1 + u_2
        u_1 = count
        u_2 = (count - u_2)
        lista.append(count)

    print(lista)
