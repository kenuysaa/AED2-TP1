from b_tree import *

def insertFilm(btree):
    print("\n--- Inserir novo filme ---")
    titulo = input("Digite o título do filme: ")
    ano = int(input("Digite o ano do filme: "))
    genero = input("Digite o gênero do filme: ")
    btree.inserir({"title": f"{titulo}", "year": ano, "genre": f"{genero}"})
    print('Filme inserido com sucesso')


def searchFilm():
    pass

def removeFilm():
    pass

def printFilm():
    pass