""" 5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
 Os métodos são os seguintes: alterarNome, depósito e saque;
 No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios."""


class ContaCorrente:
    def __init__(self, numconta, nome, saldo):
        self.numconta = numconta
        self.nome = nome
        self.saldo = saldo

    def alterarnome(self):
        self.nome = input('\nInforme o nome do correntista: ')
        self.numconta = int(input('Informe o numero da conta: '))

    def deposito(self):
        perg2 = input('Deseja realizar um deposito? [s/n]: ').lower()
        if perg2 == 's':
            deposito = float(input('Digite o valor a ser depositado: '))
            self.saldo = float(self.saldo) + deposito

    def saque(self):
        perg3 = input('Deseja realizar um saque? [s/n]: ').lower()
        if perg3 == 's':
            saque = float(input('Digite o valor a ser sacado: '))
            if saque > float(self.saldo):
                print('Saldo insuficiente, informe um valor menor ou igual a {}.'.format(self.saldo))
                saque2 = float(input('Digite o valor a ser sacado: '))
                self.saldo = float(self.saldo) - saque2
            else:
                self.saldo = float(self.saldo - saque)

    def infos(self):
        mony = '{:.2f}'.format
        print('\n----Informacoes da conta atual----\nNome: {}\nNumero da conta: {}\n'
              'Saldo: R$ {}'.format(self.nome, self.numconta, mony(self.saldo)))


def main():
    conta1 = ContaCorrente(1, 'Nome', 0)

    while True:
        conta1.alterarnome()
        conta1.deposito()
        conta1.saque()
        conta1.infos()
        continuar = input('\nDeseja realizar outra operacao? [s/n]: ').lower()
        if continuar == "n":
            print('Programa finalizado.')
            break


if __name__ == '__main__':
    main()
