from b_tree import *

def visualizarCatalogo(catalogo):
    print('|'*35)
    print("Visualizar filmes no Catalogo:")

    if not catalogo.raiz.chaves:
        print("O catalogo esta vazio. Nenhum filme foi adicionado.")
    else:
        catalogo.print_all()
    print('|'*35)

def addFilme(catalogo):
    print('|' * 35)
    print("Inserir novo filme [Digite 0 para voltar ao menu]")
    titulo = input("Digite o título do filme: ")

    if titulo == "0":
        print('|' * 35)
        return

    ano = int(input("Digite o ano do filme: "))
    genero = input("Digite o gênero do filme: ")

    filme_existe = catalogo.buscar(titulo)
    if filme_existe and filme_existe['year'] == ano and filme_existe['genre'] == genero:
        print(f"O filme '{titulo}' já existe no catálogo")
        print('|' * 35)
        return

    catalogo.inserir({"title": f"{titulo}", "year": ano, "genre": f"{genero}"})
    print('Filme inserido com sucesso!')
    print('|' * 35)

def buscar(catalogo):
    print('|' * 35)
    if not catalogo.raiz.chaves:
        print("Buscar Filme")
        print("O catalogo esta vazio. Nenhum filme foi adicionado.")
        print('|' * 35)
        return

    print("Buscar Filme [Digite 0 para voltar ao menu]")
    print("[1] - Buscar por Título")
    print("[2] - Buscar por Gênero")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        return

    if opcao == "1":
        titulo = input("Título: ")
        resultado = catalogo.buscar(titulo)
        if resultado:
            print(f"Filme encontrado: Título: {resultado['title']} ({resultado['year']}) - {resultado['genre']}")
        else:
            print(f"Filme '{titulo}' não encontrado.")

    elif opcao == "2":
        genero = input("Gênero: ")
        filmes_encontrados = catalogo.percorrer()  # Obter todos os filmes da árvore
        filmes_do_genero = [filme for filme in filmes_encontrados if filme['genre'].lower() == genero.lower()]

        if filmes_do_genero:
            print(f"Filmes encontrados no gênero '{genero}':")
            for filme in filmes_do_genero:
                print(f"Título: {filme['title']} ({filme['year']})")
        else:
            print(f"Nenhum filme de '{genero}' encontrado.")

    else:
        print("Opção inválida!")
    print('|' * 35)

def removerFilme(catalogo):
    print('|'*35)
    if not catalogo.raiz.chaves:
        print("Remover Filme")
        print("O catalogo está vazio. Não há filmes para remover.")
        print('|'*35)
        return

    print("Remover Filme do Catálogo [Digite 0 para voltar ao menu]")
    titulo = input("Digite o título do filme a ser removido: ")

    if titulo == "0":
        print('|'*35)
        return

    catalogo.remover(titulo)
    print(f"Filme '{titulo}' removido com sucesso.")
    print('|'*35)
