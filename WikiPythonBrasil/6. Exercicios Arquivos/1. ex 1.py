""" 1. Faça um programa que leia um arquivo texto contendo
uma lista de endereços IP e gere um outro arquivo, contendo um
relatório dos endereços IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256

"""

import re


def regex(pattern, string):
    capt = re.match(pattern, string)
    if bool(capt):
        return capt.group()
    return False


if __name__ == '__main__':
    ip_v = ''
    ip_i = ''
    list = {'0.25.33.19', '127.0.1.1', '127.0.0.2', '127.0.0.1', '192.0.0.256',
            '0.168.1.36', '1.1.0.99', '200.135.80.9', '192.168.1.1', '8.35.67.74',
            '257.32.4.5', '85.345.1.2', '1.2.3.4', '9.8.234.5', '192.168.0.256'}

    for ip in list:
        if ip == '0.0.0.0':
            ip_v = ip_v + '\n' + ip
        elif regex('^(([1-9]\.|[1-9][0-9]\.|1[0-9][0-9]\.|2[0-4][0-9]\.|25[0-5]\.)([0-9]\.|[1-9][0-9]\.|1[0-9]'
                   '[0-9]\.|2[0-4][0-9]\.|25[0-5]\.)([0-9]\.|[1-9][0-9]\.|1[0-9][0-9]\.|2[0-4][0-9]\.|25[0-5]\.)'
                   '([0-9]\.|[1-9][0-9]\.|1[0-9][0-9]\.|2[0-4][0-9]\.|25[0-5]\.))$', ip + '.'):
            ip_v = ip_v + '\n' + ip
        else:
            ip_i = ip_i + '\n' + ip

    print('[Endereços válidos:]')
    print(ip_v)
    print('[Endereços inválidos:]')
    print(ip_i)
