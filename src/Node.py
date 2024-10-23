class Node:
    def __init__(self, ordem, folha=False):
        # self.ordem = ordem
        self.chave = []
        self.filho = []
        self.folha = folha
    
    def __str__(self):
        return str(self.chaves)