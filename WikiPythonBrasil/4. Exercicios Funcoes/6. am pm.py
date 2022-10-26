""" 6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para
novos valores de entrada todas as vezes que desejar.
"""


if __name__ == '__main__':
    while True:
        hora = int(input('Digite a hora no formato XX: '))
        minuto = str(input('Digite o minuto no formato XX: '))
        ampm = (input('Digite A para AM e P para PM: '))
        info = ampm.upper()


        def conversao(hora1, minuto1, info1):
            if info1 == 'P':
                if hora1 > 12:
                    hconv = hora1 - 12
                    return f'Horario convertido: {hconv}:{minuto1} P.M'
                if hora1 < 13:
                    print('A hora informada nao precisou de conversao!')
                    return f'{hora1}:{minuto1} P.M'

            if info1 == 'A':
                if hora1 <= 12:
                    print('A hora informada nao precisou de conversao!')
                    return f'{hora1}:{minuto1} A.M'
                else:
                    print('Horario invalido, reinicie o programa!')
                    exit()


        def saida(hr, minuto2, info2):
            print(conversao(hr, minuto2, info2))


        saida(hora, minuto, info)
