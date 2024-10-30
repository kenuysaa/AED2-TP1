from b_tree import *
from menu import *

if __name__ == "__main__":
    # Inicialize a árvore B com a ordem mínima desejada (exemplo: t=3)
    btree = B_Tree(ordem=3)
    
    # Inserir dados dos filmes
    insertFilm(btree)

    # Buscar um filme específico
    title_to_search = "Inception"
    result = btree.buscar(title_to_search)
    if result:
        print(f"Filme encontrado: Título: {result['title']}, Ano: {result['year']}, Gênero: {result['genre']}")
    else:
        print(f"Filme '{title_to_search}' não encontrado.")

    # Imprimir todos os filmes
    print("\nTodos os filmes na árvore B:")
    btree.print_all()
    print('a'*20)
    btree.remover("Inception")
    btree.print_all()
    save_to_excel(btree)
