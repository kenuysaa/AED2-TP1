class Filme:
    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero

    def __str__(self):
        return f"{self.titulo}, {self.ano} - {self.genero}"
        