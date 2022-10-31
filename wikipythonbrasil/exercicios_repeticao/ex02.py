""" 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""


if __name__ == '__main__':
    nome = str(input('Digite o nome de usuario: '))
    senha = str(input('Digite a senha: '))

    while nome == senha:
        print('A senha deve ser diferente do nome de usuario! ')
        nome = str(input('Digite o nome de usuario: '))
        senha = str(input('Digite a senha: '))

    else:
        print('Usuario cadastrado com sucesso! ')
