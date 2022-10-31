""" 13. Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

for i in range(len(temp_lista)):
 print(f'{i}|{temp_lista[i]}')
"""


if __name__ == '__main__':
    meses = ["janeiro", "fevereiro", "março", "abril", "maio",
             "junho", "julho", "agosto", "setembro", "outubro",
             "novembro", "dezembro"]

    temperaturas = []

    for i in range(12):
        temperaturas.append(float(input(f"Digite a temperatura de {meses[i]} em ºC: ")))

    media = sum(temperaturas) / 12

    print(f"\nA média das temperaturas do ano é {media:.2f}ºC.")
    print("Meses com temperaturas acima da média: ")

    for i in range(12):
        if temperaturas[i] > media:
            print(f"{i+1} - {meses[i].capitalize()} : {temperaturas[i]:.2f}ºC")
