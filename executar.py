import csv
import matplotlib.pyplot as plt
import time

from arvore import HashTable as HashTableArvore
from encad import HashTable as HashTableLivre

CAPACIDADE = 15000 # Capacidade definida 
tabela_com_arvore = HashTableArvore(CAPACIDADE)
tabela_com_livre = HashTableArvore(CAPACIDADE)

# INSERÇÃO:
tempo_final_arvore = 0
tempo_final_livre = 0

# BUSCA:
tempo_busca_arvore = 0
tempo_busca_livre = 0

# REMOÇÃO:
tempo_remocao_arvore = 0
tempo_remocao_livre = 0

# INSERCAO ARVORE E LIVRE
print('Processando insercoes...')
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

# BUSCA ARVORE E LIVRE
print('\nProcessando buscas...')
with open('busca.csv', mode='r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        cpf = int(linha[0])
        
        inicio_arvore = time.perf_counter()
        tabela_com_arvore.tabela_pesquisa(cpf)
        fim_arvore = time.perf_counter()
        tempo_busca_arvore += (fim_arvore - inicio_arvore)

        inicio_livre = time.perf_counter()
        tabela_com_livre.tabela_pesquisa(cpf)
        fim_livre = time.perf_counter()
        tempo_busca_livre += (fim_livre - inicio_livre)

print(f"Tempo total de busca na Árvore: {tempo_busca_arvore:.6f} segundos")
print(f"Tempo total de busca no Enc. Livre: {tempo_busca_livre:.6f} segundos")


# BUSCA ARVORE E LIVRE
print('\nProcessando remover...')
with open('remocao.csv', mode='r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        cpf = int(linha[0])
        
        inicio_arvore = time.perf_counter()
        try:
            tabela_com_arvore.tabela_remover(cpf)
        except KeyError:
            pass

        fim_arvore = time.perf_counter()
        tempo_remocao_arvore += (fim_arvore - inicio_arvore)

        inicio_livre = time.perf_counter()
        try:
            tabela_com_livre.tabela_remover(cpf)
        except KeyError:
            pass

        fim_livre = time.perf_counter()
        tempo_remocao_livre += (fim_livre - inicio_livre)

print(f"Tempo total de remocao na Árvore: {tempo_remocao_arvore:.6f} segundos")
print(f"Tempo total de remocao no Enc. Livre: {tempo_remocao_livre:.6f} segundos")


# GERANDO OS GRAFICOS

operacoes = ['Inserção', 'Busca', 'Remoção']


tempos_arvore = [tempo_final_arvore, tempo_busca_arvore, tempo_remocao_arvore]
tempos_livre = [tempo_final_livre, tempo_busca_livre, tempo_remocao_livre]

x = range(len(operacoes))
largura = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

# Desenha as barras de cada estrutura
barra1 = ax.bar([i - largura/2 for i in x], tempos_arvore, largura, label='Hash + Árvore BST', color='#1f77b4')
barra2 = ax.bar([i + largura/2 for i in x], tempos_livre, largura, label='Hash + End. Livre', color='#ff7f0e')

# Customização visual do gráfico
ax.set_ylabel('Tempo Total de Execução (segundos)', fontsize=12)
ax.set_title('Comparativo de Desempenho: Árvore BST vs Endereçamento Livre', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(operacoes, fontsize=11)
ax.legend(fontsize=11)
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Mostra o gráfico na tela e salva automaticamente um arquivo de imagem na pasta
plt.tight_layout()
plt.savefig('grafico_desempenho.png', dpi=300)
plt.show()