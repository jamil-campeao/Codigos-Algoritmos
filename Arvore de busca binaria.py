import csv

class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

def construir_arvore_binaria(dados):
    raiz = None

    for dado in dados:
        chave = dado[1]

        if raiz is None:
            raiz = No(chave)
        else:
            inserir_na_arvore(raiz, chave)

    return raiz

def inserir_na_arvore(raiz, chave):
    if chave < raiz.chave:
        if raiz.esquerda is None:
            raiz.esquerda = No(chave)
        else:
            inserir_na_arvore(raiz.esquerda, chave)
    else:
        if raiz.direita is None:
            raiz.direita = No(chave)
        else:
            inserir_na_arvore(raiz.direita, chave)

def busca_arvore_binaria(raiz, chave_procurada):
    if raiz is None or raiz.chave == chave_procurada:
        return raiz

    if chave_procurada < raiz.chave:
        return busca_arvore_binaria(raiz.esquerda, chave_procurada)
    else:
        return busca_arvore_binaria(raiz.direita, chave_procurada)

def exibir_arvore_em_ordem(raiz):
    if raiz is not None:
        exibir_arvore_em_ordem(raiz.esquerda)
        print(raiz.chave)
        exibir_arvore_em_ordem(raiz.direita)

dados = []
with open('nascidosbrasil.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        dados.append(linha)

arvore_binaria = construir_arvore_binaria(dados)

exibir_arvore_em_ordem(arvore_binaria)
x = 1

while x == 1:
    chave_procurada = input("\nDigite um nome: \n")
    pesquisa = busca_arvore_binaria(arvore_binaria, chave_procurada)
    if pesquisa is not None:
        print("\n O nome {} foi encontrado".format(chave_procurada))
    else:
        print("\nO nome {} não foi encontrado".format(chave_procurada))

    x = int(input("\nDIGITE 1 PARA UMA NOVA PESQUISA OU 0 PARA SAIR\n"))