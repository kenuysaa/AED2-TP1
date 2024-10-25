class Node:
    def __init__(self, ordem, folha=False): # pq folhas=False?
        self.filmes = []
        self.filho = []
        self.folha = folha
        self.ordem = ordem # (t)
    
    def __str__(self):
        return "; ".join([str(filme) for filme in self.filmes])