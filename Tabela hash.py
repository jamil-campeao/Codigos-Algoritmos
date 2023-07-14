import csv

tabela_hash = {}

with open('nascidosbrasil.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    for linha in leitor_csv:
        nome = linha[1]

        tabela_hash[nome] = nome

x = 1

while x == 1:
    nome_pesquisa = input("\nDigite um nome para pesquisar: \n")

    if nome_pesquisa in tabela_hash:
        resultado = tabela_hash[nome_pesquisa]
        print("\nO nome {} foi encontrado".format(resultado))
    else:
        print("Nome não encontrado na tabela")

    x = int(input("\nDIGITE 1 PARA UMA NOVA PESQUISA OU 0 PARA SAIR\n"))
