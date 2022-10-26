""" Utilize uma lista para resolver o problema a seguir.
Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
 Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana
 recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
 Escreva um programa (usando um array de contadores) que determine quantos vendedores
  receberam salários nos seguintes intervalos de valores:
  $200 - $299
  $300 - $399
  $400 - $499
  $500 - $599
  $600 - $699
  $700 - $799
  $800 - $899
  $900 - $999
  $1000 em diante """


if __name__ == '__main__':
    lista = []
    contagem_de_faixa_salarial = [0] * 9
    for i in range(3):
        venda = int(input('Digite o valor de venda bruta: '))
        total = int(200 + (venda * 0.09))
        lista.append(total)

    for salario in lista:
        indice = salario // 100 - 2  # formula para alocar cada salario em um indice
        indice_maximo = len(contagem_de_faixa_salarial) - 1  # usado para fixar um indice maximo
        indice = min(indice, indice_maximo)  # usado para fixar um indice minimo
        contagem_de_faixa_salarial[indice] += 1  # aumenta a contagem nos indices

    print(contagem_de_faixa_salarial)
