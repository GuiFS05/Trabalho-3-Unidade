class NoBST:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None

class HashTable:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tamanho = 0
        self.tabela = [None] * capacidade

    def _hash(self, chave):
        return hash(chave) % self.capacidade
    
    def tabela_inserir(self, chave, valor):
        indice = self._hash(chave)

        if self.tabela[indice] is None:
            self.tabela[indice] = NoBST(chave, valor)
            self.tamanho += 1
        else:
            self.tabela[indice], inseriu_novo = self._inserir_bst(self.tabela[indice], chave, valor)
            if inseriu_novo:
                self.tamanho += 1
                
    def _inserir_bst(self, no, chave, valor):
        if no is None:
            return NoBST(chave, valor), True
        
        if chave == no.chave:
            no.valor = valor
            return no, False
        
        elif chave < no.chave:
            no.esquerda, inseriu = self._inserir_bst(no.esquerda, chave, valor)
        else:
            no.direita, inseriu = self._inserir_bst(no.direita, chave, valor)
            
        return no, inseriu

    def tabela_pesquisa(self, chave):
        indice = self._hash(chave)
        no_encontrado = self._pesquisa_bst(self.tabela[indice], chave)
        
        if no_encontrado:
            return no_encontrado.valor
        raise KeyError(f"Chave '{chave}' não encontrada.")

    def _pesquisa_bst(self, no, chave):
        if no is None:
            return None
        
        if chave == no.chave:
            return no
        elif chave < no.chave:
            return self._pesquisa_bst(no.esquerda, chave)
        else:
            return self._pesquisa_bst(no.direita, chave)

    def tabela_remover(self, chave):
        self.tabela_pesquisa(chave) 
        indice = self._hash(chave)
        self.tabela[indice] = self._remover_bst(self.tabela[indice], chave)
        self.tamanho -= 1

    def _remover_bst(self, no, chave):
        if no is None:
            return no
        if chave < no.chave:
            no.esquerda = self._remover_bst(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover_bst(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            sucessor = self._min_valor_no(no.direita)
            no.chave = sucessor.chave
            no.valor = sucessor.valor
            no.direita = self._remover_bst(no.direita, sucessor.chave)
        return no

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual