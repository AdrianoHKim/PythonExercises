""" 3. Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'.
"""


if __name__ == '__main__':
    nome = str(input('Digite o nome: '))

    while len(nome) <= 3:
        print('Nome invalido, deve conter mais de 3 caracteres!')
        nome = input('Digite o nome: ')

    idade = int(input('Digite a idade: '))

    while idade > 150 or idade < 0:
        print('Idade invalida, digite uma idade entre 0 e 150')
        idade = int(input('Digite a idade: '))

    salario = float(input('Digite o salario: '))

    while salario < 0:
        print('Salario invalido, deve ser maior que 0!')
        salario = float(input('Digite o salario: '))

    sexo = str.lower(input('Digite o sexo | f - feminino | m - masculino: '))

    while sexo != 'f' and sexo != 'm':
        print('Sexo invalido!')
        sexo = str(input('Digite o sexo | f - feminino | m - masculino: '))

    estado = str.lower(input('Digite o estado civil\ns - solteiro(a)\nc - casado(a)\n'
                             'v - viuvo(a)\nd - divorciado(a)\n==> '))

    while estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
        print('Estado civil invalido!')
        estado = str.lower(input('Digite o estado civil | s - solteiro(a)\nc - casado(a)\n'
                                 'v - viuvo(a)\nd - divorciado(a)\n==> '))

    print('Dados cadastrados com sucesso! ')
