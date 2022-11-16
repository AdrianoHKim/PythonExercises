""" 6. Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""


class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def alterarcanal(self):
        print('Canal atual: {}'.format(self.canal))
        self.canal = int(input('Mudar para o canal: '))
        if self.canal > 100:
            self.canal = int(input('Canal invalido, digite um canal de 1 a 100: '))
        else:
            print('Canal atual: {}'.format(self.canal))

    def alterarvolume(self):
        print('Volume atual: {}'.format(self.volume))
        volume = int(input('Alterar volume: '))
        if self.volume > volume >= 0:
            self.volume = volume
            print('Volume diminuido para: {}'.format(self.volume))

        if self.volume < volume <= 20:
            self.volume = volume
            print('Volume aumentado para: {}'.format(self.volume))

        if volume < 0 or volume > 20:
            print('Volume invalido, digite um valor entre 1 e 20: ')
            volume = int(input('Alterar volume: '))
            if self.volume > volume >= 0:
                self.volume = volume
                print('Volume diminuido para: {}'.format(self.volume))

            if self.volume < volume <= 20:
                self.volume = volume
                print('Volume aumentado para: {}'.format(self.volume))


def main():
    tv1 = Tv(1, 10)

    while True:
        opcao = int(input('---- Menu ----\n1 - Alterar canal\n2 - Alterar volume\n3 - Sair\nDigite a opcao: '))
        if opcao == 1:
            tv1.alterarcanal()
        if opcao == 2:
            tv1.alterarvolume()
        if opcao == 3:
            print('Menu finalizado.')
            break
        else:
            print('Opcao invalida')


if __name__ == '__main__':
    main()
