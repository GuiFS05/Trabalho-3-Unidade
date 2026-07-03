class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class HashTable:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tamanho = 0
        self.tabela = [None]*capacidade

    def _hash(self, chave):
        return hash(chave) % self.capacidade #Por que esse índice é retornado?
    
    def tabela_inserir(self, chave, valor):
        indice = self._hash(chave)

        if self.tabela[indice] is None:
            self.tabela[indice] = No(chave, valor)
            self.tamanho += 1
        else:
            atual = self.tabela[indice]
            while atual:
                if atual.key == chave:
                    atual.valor = valor
                    return
                atual = atual.proximo
            novo_nodo = No(chave, valor)
            novo_nodo.proximo = self.tabela[indice]
            self.tabela[indice] = novo_nodo
            self.tabela += 1
    
    def tabela_pesquisa(self, chave):
        indice = self._hash(chave)

        agora = self.tabela[indice]
        while agora:
            if agora.chave == chave:
                return agora.valor
            agora = agora.proximo
        raise KeyError(chave)
    
    def tabela_remover(self, chave):
        indice = self._hash(chave)

        anterior = None
        agora = self.tabela[indice]

        while agora:
            if agora.chave == chave:
                if anterior:
                    anterior.proximo = agora.proximo
                else:
                    self.tabela[indice] = agora.proximo
                self.tamanho-= 1
                return
            anterior = agora
            agora = agora.proximo

        raise KeyError(chave)