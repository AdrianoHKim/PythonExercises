""" 9. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de
CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação
dos dígitos verificadores edos caracteres de formatação.

"""


def verificarnumeros(cpf):
    for posicao, caractere in enumerate(cpf):
        if posicao != 3 and posicao != 7 and posicao != 11 and not caractere.isdigit():
            return True


if __name__ == '__main__':
    cpf1 = input('Digite o CPF no formato (xxx.xxx.xxx-xx): ')

    while len(cpf1) < 13 or verificarnumeros(cpf1) or cpf1[3] != '.' or cpf1[7] != '.' or cpf1[11] != '-':
        cpf1 = input('CPF invalido!\nDigite o CPF no formato (xxx.xxx.xxx-xx) :')

    print('O CPF foi cadastrado com sucesso.')
