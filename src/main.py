from b_tree import *
from menu import *

if __name__ == "__main__":
    catalogo = B_Tree(ordem=3)

    while True:
        print('-'*35)
        print("| Catalogo de Filmes")
        print("| [1] - Visualizar Catalogo")
        print("| [2] - Adicionar novo filme")
        print("| [3] - Buscar Filme")
        print("| [4] - Remover Filme do Catalogo")
        print("| [0] - Encerrar Programa")
        print('-'*35)
        
        try:
            opc = int(input("Escolha uma opçõa: "))
        except ValueError:
            print("Valor invalido! Digite um número de 0 a 4")
            continue
        print('\n')
        match opc:
            case 1:
                visualizarCatalogo(catalogo)
            case 2:
                addFilme(catalogo)
            case 3:
                buscar(catalogo)
            case 4:
                removerFilme(catalogo)
            case 0:
                print("Programa encerrado")
                break
            case _:
                print("Opção invalida!")

    # Buscar um filme específico
    #title_to_search = "Inception"
    #result = catalogo.buscar(title_to_search)
    #if result:
    #    print(f"Filme encontrado: Título: {result['title']}, Ano: {result['year']}, Gênero: {result['genre']}")
    #else:
    #   print(f"Filme '{title_to_search}' não encontrado.")

    # print('a'*20)
    # catalogo.remover("Inception")
    # catalogo.print_all()
    save_to_excel(catalogo)