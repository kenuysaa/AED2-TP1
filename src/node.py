# registros = no minimo a ordem e no maximo ordem*2, exceto a raiz que podeter no minimo 1 registro
class Node:
    def __init__(self, ordem, folhas=False):
        self.ordem = ordem # (t)
        self.folhas = folhas
        self.chaves = [] # registros de filmes
        self.filhos = []
    
    def __str__(self):
        return "; ".join([str(filme) for filme in self.filmes])