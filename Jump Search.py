import csv
import math

def jump_search(lista, valor_procurado):
    tamanho = len(lista)
    salto = int(math.sqrt(tamanho))
    anterior = 0
    atual = salto

    while atual < tamanho and lista[atual] < valor_procurado:
        anterior = atual
        atual += salto

    for i in range(anterior, min(atual + 1, tamanho)):
        if lista[i] == valor_procurado:
            return i

    return -1

lista = []

with open('nascidosbrasil.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        nome = linha[1]
        lista.append(nome)

x = 1

while x == 1:
    pesquisa = input("\nDigite um nome: ")
    indice = jump_search(lista, pesquisa)

    if indice != -1:
        print("O Nome", pesquisa, "foi encontrado no índice", indice)
    else:
        print("O Nome", pesquisa, "não foi encontrado na lista")

    x = int(input("\nDIGITE 1 PARA UMA NOVA PESQUISA OU 0 PARA SAIR\n"))
