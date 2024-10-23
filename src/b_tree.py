from Node import Node

class B_Tree:
    def __int__(self, ordem):
        self.raiz = Node(folha=True)
        self.ordem = ordem
    
    def __init__(self, ordem):
        self.raiz = Node(ordem, folha=True)  # Inicializa a árvore com a raiz como folha
        self.ordem = ordem  # Ordem da árvore B (grau mínimo)
    
    # Inserir uma chave na árvore
    def inserir(self, chave):
        raiz = self.raiz
        # Verifica se a raiz está cheia (contém 2 * ordem - 1 chaves)
        if len(raiz.chaves) == (2 * self.ordem) - 1:
            # Se estiver cheia, cria um novo nó temporário e define-o como raiz
            novo_no = Node(self.ordem, folha=False)
            novo_no.filhos.append(self.raiz)  # O novo nó terá a raiz original como filho
            self.dividir_no(novo_no, 0)  # Divide a raiz original
            self.inserir_nao_cheio(novo_no, chave)  # Insere a chave no novo nó
            self.raiz = novo_no  # Atualiza a raiz para o novo nó
        else:
            self.inserir_nao_cheio(raiz, chave)

    # Função para dividir um nó filho cheio
    def dividir_no(self, no_pai, indice_filho):
        ordem = self.ordem
        no_cheio = no_pai.filhos[indice_filho]
        novo_no = Node(ordem, folha=no_cheio.folha)  # Cria um novo nó para armazenar metade das chaves

        # Movendo as chaves e filhos de no_cheio para novo_no
        no_pai.filhos.insert(indice_filho + 1, novo_no)
        no_pai.chaves.insert(indice_filho, no_cheio.chaves[ordem - 1])

        # Dividindo as chaves
        novo_no.chaves = no_cheio.chaves[ordem:(2 * ordem - 1)]
        no_cheio.chaves = no_cheio.chaves[0:(ordem - 1)]

        # Se o nó não for folha, também movemos os filhos
        if not no_cheio.folha:
            novo_no.filhos = no_cheio.filhos[ordem:(2 * ordem)]
            no_cheio.filhos = no_cheio.filhos[0:(ordem - 1)]


    # buscar
    # remover