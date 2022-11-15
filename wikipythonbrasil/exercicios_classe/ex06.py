""" 6. Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""


class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def alterarcanal(self):
        self.canal = int(input('Digite o canal desejado: '))
        if self.canal > 100:
            self.canal = int(input('Canal invalido, digite um canal de 1 a 100:'))

