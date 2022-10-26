""" 8. Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor. Imprima a idade
e a altura na ordem inversa a ordem lida."""


if __name__ == '__main__':
    lista = []

    for i in range(5):
        idade = input('Digite a idade: ')
        altura = input('Digite a altura: ')
        lista.append(idade)
        lista.append(altura)
    lista.reverse()
    print(lista)
