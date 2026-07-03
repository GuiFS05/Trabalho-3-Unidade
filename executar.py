import csv
import matplotlib
import time

from arvore import HashTable as HashTableArvore
from encad import HashTable as HashTableLivre

CAPACIDADE = 15000 # Capacidade definida 
tabela_com_arvore = HashTableArvore(CAPACIDADE)
tabela_com_livre = HashTableArvore(CAPACIDADE)

# INSERCAO ARVORE
print('Processando insercoes')
inicio_arvore = time.perf_counter()

with open('insercao.csv', mode='r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        cpf = int(linha[0])
        dados = linha[1:]
        tabela_com_arvore.tabela_inserir(cpf, dados)

fim_arvore = time.perf_counter()
tempo_arvore = fim_arvore - inicio_arvore
