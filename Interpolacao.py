import csv

def pesquisa_interpolacao(lista, valor_procurado):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita and lista[esquerda] <= valor_procurado <= lista[direita]:
        posicao = esquerda + ((direita - esquerda) // (lista[direita] - lista[esquerda])) * (valor_procurado - lista[esquerda])

        if lista[posicao] == valor_procurado:
            return posicao
        elif lista[posicao] < valor_procurado:
            esquerda = posicao + 1
        else:
            direita = posicao - 1


    return -1

lista = []

with open('nascidosbrasil.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    for linha in leitor_csv:
        valor = int(linha[2])
        lista.append(valor)

lista_ord = sorted(lista)

for var in lista_ord:
    print(var)

x = 1
while x == 1:
    pesquisa = int(input("\nDigite um Valor: "))

    resultado = pesquisa_interpolacao(lista_ord, pesquisa)

    if resultado != -1:
        print("O valor", pesquisa, "foi encontrado no índice", resultado)
    else:
        print("O valor", pesquisa, "não foi encontrado na lista")

    x = int(input("\nDIGITE 1 PARA UMA NOVA PESQUISA OU 0 PARA SAIR\n"))