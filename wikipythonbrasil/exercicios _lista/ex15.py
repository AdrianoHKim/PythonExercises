""" 15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
 Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem"""


if __name__ == '__main__':
    lista = []

    while True:
        numero = int(input('Digite um numero: '))
        if numero == -1:
            break
        lista.append(numero)

    print(f'A quantidade de valores lidos é: {len(lista)}.')
    print(lista)

    rev = reversed(lista)

    for i in rev:
        print(i)

    print(f'A soma dos valores lidos é: {sum(lista)}.')

    media = sum(lista)/len(lista)
    print(f'A media dos valores lidos é: {media}.')

    print('Os valores acima da media é/sao:', ', '.join(str(med) for med in lista if med > media))

    print('Os valores abaixo de sete é/sao:', ', '.join(str(abaixo) for abaixo in lista if abaixo < 7))

    print('Vlvv flvvv!')
