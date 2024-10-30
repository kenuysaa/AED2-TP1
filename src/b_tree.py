from node import Node

class B_Tree:
    def __init__(self, ordem):
        self.raiz = Node(folhas=True)
        self.ordem = ordem

    #### inserir novo no ###
    def inserir(self, chave):
        raiz = self.raiz
        # se a quantidade de chaves for igual a 2m
        # cria nova raiz e divide
        if len(raiz.chaves) == (2 * self.ordem):
            nova_raiz = Node(self.ordem, folhas=False)
        else:
            self._inserir_nao_cheio(raiz, chave)
    
    def _dividir_node(self, node_pai, i): # node com maximo de registros
        ordem = self.ordem
        node_cheio = node_pai.filhos[i]
        node_novo = Node(ordem, folhas=node_cheio.folhas)

        node_pai.filhos.inserir(i + 1, node_novo)
        node_pai.chaves.inserir(i, node_cheio.chaves[ordem - 1])

        # criar uma nova lista a partir de um subconjunto da lista original
        # facilitando a divisão das chaves durante a operação de divisão de um nó em uma árvore B
        node_novo.chaves = node_cheio.chaves[ordem:]
        node_cheio.chaves = node_cheio.chaves[:ordem - 1]

        if not node_cheio.folhas: # se não for node interno
            node_novo.filhos = node_cheio.filhos[ordem:]
            node_cheio.filhos = node_cheio.filhos[:ordem]

    def _inserir_nao_cheio(self, node, chave)
        i = len(node.chaves) - 1 # quantidade de chaves e aponta para o ultimo indice do nodo (-1)

        if node.folhas: # o node é uma folha
            node.chaves.append(None) # cria um espaço no final da lista para add chave, facilita o processo de deslocamento
            while i >= 0 and chave < node.chaves[i]: # percorre as chaves da direita pra esquerda
                node.chaves[i+1] = node.chaves[i] # desloca a chave
                i -= 1
            node.chaves[i+1] = chave # adiciona a chave no seu lugar

        else: # node interno que tem filhos
            while i >= 0 and chave < node.chaves[i]:
                i -= 1
            i += 1

            if len(node.filhos[i].chaves) == (2 * self.ordem)
                self._dividir_node(node, i)
                if chave > node.chaves[i]
                    i += 1
            self._inserir_nao_cheio(node.filhos[i], chave)

    # buscar
    # remover