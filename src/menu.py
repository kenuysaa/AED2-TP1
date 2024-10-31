from b_tree import *

def vizualizarCatalogo(catalogo):
    print("\nTodos os filmes na árvore B:")
    catalogo.print_all()

def addFilme(catalogo):
    print("\n--- Inserir novo filme [Digite 0 para volta ao menu] ---")
    titulo = input("Digite o título do filme: ")

    if titulo == "0":
        return

    ano = int(input("Digite o ano do filme: "))
    genero = input("Digite o gênero do filme: ")
    catalogo.inserir({"title": f"{titulo}", "year": ano, "genre": f"{genero}"})
    print('Filme inserido com sucesso')

def buscarTitulo(catalogo):
    print("\n--- Buscar Filme por Titulo ---")
    titulo = input("Titulo: ")
    catalogo.buscar(titulo)

def removerFilme(catalogo):
    pass
