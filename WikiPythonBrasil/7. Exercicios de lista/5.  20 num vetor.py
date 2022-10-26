""" 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores."""


if __name__ == '__main__':
    todos = []
    par = []
    impar = []

    for i in range(20):
        numero = int(input('Digite um numero: '))
        if numero % 2 == 0:
            todos.append(numero)
            par.append(numero)

        else:
            todos.append(numero)
            impar.append(numero)

    print(f'Todos numeros digitados: {todos}, \nTodos numeros pares: {par}\n'
          f'Todos numeros impares: {impar}')
