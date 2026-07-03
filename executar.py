import csv
import matplotlib
import time

from arvore import HashTable as HashTableArvore
from encad import HashTable as HashTableLivre

CAPACIDADE = 15000 # Capacidade definida 
tabela_com_arvore = HashTableArvore(CAPACIDADE)
tabela_com_livre = HashTableArvore(CAPACIDADE)

tempo_final_arvore = 0
tempo_final_livre = 0

# INSERCAO ARVORE
print('Processando insercoes')
with open('insercao.csv', mode='r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        cpf = int(linha[0])
        dados = linha[1:]
        
        inicio_arvore = time.perf_counter()
        tabela_com_arvore.tabela_inserir(cpf, dados)
        fim_arvore = time.perf_counter()
        tempo_final_arvore += (fim_arvore - inicio_arvore)

        inicio_livre = time.perf_counter()
        tabela_com_livre.tabela_inserir(cpf, dados)
        fim_livre = time.perf_counter()
        tempo_final_livre += (fim_livre - inicio_livre)

print(f"Tempo total de inserção na Árvore: {tempo_final_arvore:.6f} segundos")
print(f"Tempo total de inserção no Enc. Livre: {tempo_final_livre:.6f} segundos")
