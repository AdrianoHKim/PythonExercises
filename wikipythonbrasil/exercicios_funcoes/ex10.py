""" 10.Jogo de Craps. Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
 Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
  Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
  Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente."""

import time
from random import randint


if __name__ == '__main__':
    def craps():
        dado = randint(2, 12)
        if dado == 7 or dado == 11:
            print(f'Resultado: {dado}, NATURAL! voce ganhou!')
        elif dado == 2 or dado == 3 or dado == 12:
            print(f'Resultado: {dado}, CRAPS! voce perdeu!')
        elif dado in range(4, 6) or dado in range(8, 10):
            print(f'Resultado: {dado}, PONTO! jogue novamente!')
            dado2 = 0
            while dado != dado2:
                time.sleep(1)
                dado2 = randint(2, 12)
                if dado2 == 7:
                    print(f'Resultado: {dado2}, voce perdeu!')
                    break
                if dado != dado2:
                    print(f'Resultado: {dado2}, jogando novamente:')
            else:
                print(f'Resultado: {dado2}, PONTO novamente, voce ganhou!')


    craps()
