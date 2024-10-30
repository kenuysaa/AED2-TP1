from node import Node
from openpyxl import Workbook

class B_Tree:
    def __init__(self, ordem):
        self.raiz = Node()
        self.ordem = ordem  # ordem mínima

######################### INSERIR ########################
    def inserir(self, chave):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.ordem) - 1:
            nova_raiz = Node(folha=False)
            nova_raiz.filhos.append(raiz)
            self._dividir_filho(nova_raiz, 0)
            self.raiz = nova_raiz
        self._inserir_nao_cheio(self.raiz, chave)

    def _inserir_nao_cheio(self, node, chave):
        if node.folha:
            node.chaves.append(chave)
            node.chaves.sort(key=lambda x: x["title"])
        else:
            i = len(node.chaves) - 1
            while i >= 0 and chave["title"] < node.chaves[i]["title"]:
                i -= 1
            i += 1
            if len(node.filhos[i].chaves) == (2 * self.ordem) - 1:
                self._dividir_filho(node, i)
            self._inserir_nao_cheio(node.filhos[i], chave)

    def _dividir_filho(self, pai, i):
        ordem = self.ordem
        filho = pai.filhos[i]
        novo_filho = Node(folha=filho.folha)
        pai.chaves.insert(i, filho.chaves[ordem - 1])
        pai.filhos.insert(i + 1, novo_filho)
        novo_filho.chaves = filho.chaves[ordem:]
        filho.chaves = filho.chaves[:ordem - 1]
        if not filho.folha:
            novo_filho.filhos = filho.filhos[ordem:]
            filho.filhos = filho.filhos[:ordem]

    ######################### REMOVER ########################
    def remover(self, chave):
        self._remover_interno(self.raiz, chave)
        # Ajusta a raiz se o nó ficar vazio após remoção
        if len(self.raiz.chaves) == 0:
            if not self.raiz.folha:
                self.raiz = self.raiz.filhos[0]
            else:
                self.raiz = Node(folha=True)

    def _remover_interno(self, node, chave):
        idx = self._encontrar_chave(node, chave)

        # Caso 1: A chave está node nó folha
        if idx < len(node.chaves) and node.chaves[idx]["title"] == chave:
            if node.folha:
                node.chaves.pop(idx)
            else:
                self._remover_interno_nao_folha(node, idx)
        else:
            # Se estamos em um nó folha e a chave não está presente
            if node.folha:
                print("A chave não está presente na árvore")
                return

            # Caso 2: A chave não está node nó e precisa ser procurada nos filhos
            eh_ultimo_filho = (idx == len(node.chaves))
            if len(node.filhos[idx].chaves) < self.ordem:
                self._preencher(node, idx)

            # Recurte para o filho apropriado (após o preenchimento, se necessário)
            if eh_ultimo_filho and idx > len(node.chaves):
                self._remover_interno(node.filhos[idx - 1], chave)
            else:
                self._remover_interno(node.filhos[idx], chave)

    def _remover_interno_nao_folha(self, node, idx):
        chave = node.chaves[idx]

        # Caso 3A: O predecessor tem pelo menos ordem chaves
        if len(node.filhos[idx].chaves) >= self.ordem:
            chave_pred = self._get_predecessor(node, idx)
            node.chaves[idx] = chave_pred
            self._remover_interno(node.filhos[idx], chave_pred["title"])

        # Caso 3B: O sucessor tem pelo menos ordem chaves
        elif len(node.filhos[idx + 1].chaves) >= self.ordem:
            chave_succ = self._get_successor(node, idx)
            node.chaves[idx] = chave_succ
            self._remover_interno(node.filhos[idx + 1], chave_succ["title"])

        # Caso 3C: Fusão dos filhos
        else:
            self._unir(node, idx)
            self._remover_interno(node.filhos[idx], chave["title"])

    def _get_predecessor(self, node, idx):
        cur = node.filhos[idx]
        while not cur.folha:
            cur = cur.filhos[-1]
        return cur.chaves[-1]

    def _get_successor(self, node, idx):
        cur = node.filhos[idx + 1]
        while not cur.folha:
            cur = cur.filhos[0]
        return cur.chaves[0]

    def _preencher(self, node, idx):
        if idx != 0 and len(node.filhos[idx - 1].chaves) >= self.ordem:
            self._pegar_do_anterior(node, idx)
        elif idx != len(node.chaves) and len(node.filhos[idx + 1].chaves) >= self.ordem:
            self._pegar_do_proximo(node, idx)
        else:
            if idx != len(node.chaves):
                self._unir(node, idx)
            else:
                self._unir(node, idx - 1)

    def _pegar_do_anterior(self, node, idx):
        filho = node.filhos[idx]
        irmao = node.filhos[idx - 1]

        filho.chaves.insert(0, node.chaves[idx - 1])
        if not filho.folha:
            filho.filhos.insert(0, irmao.filhos.pop())

        node.chaves[idx - 1] = irmao.chaves.pop()

    def _pegar_do_proximo(self, node, idx):
        filho = node.filhos[idx]
        irmao = node.filhos[idx + 1]

        filho.chaves.append(node.chaves[idx])
        if not filho.folha:
            filho.filhos.append(irmao.filhos.pop(0))

        node.chaves[idx] = irmao.chaves.pop(0)

    def _unir(self, node, idx):
        filho = node.filhos[idx]
        irmao = node.filhos[idx + 1]

        filho.chaves.append(node.chaves.pop(idx))
        filho.chaves.extend(irmao.chaves)
        if not filho.folha:
            filho.filhos.extend(irmao.filhos)

        node.filhos.pop(idx + 1)

    def _encontrar_chave(self, node, chave_title):
        idx = 0
        while idx < len(node.chaves) and node.chaves[idx]["title"] < chave_title:
            idx += 1
        return idx

######################### BUSCAR ########################
    def buscar(self, title):
        # Inicia a busca a partir da raiz
        return self._buscar_no(self.raiz, title)

    def _buscar_no(self, node, title):
        # Encontra o índice da chave ou o ponto onde a chave estaria
        i = 0
        while i < len(node.chaves) and title > node.chaves[i]["title"]:
            i += 1

        # Caso 1: A chave está node nó atual
        if i < len(node.chaves) and node.chaves[i]["title"] == title:
            return node.chaves[i]

        # Caso 2: Chegamos ao final sem encontrar e estamos em uma folha
        if node.folha:
            return None

        # Caso 3: Se a chave não está node nó e ele não é folha, busca node filho apropriado
        return self._buscar_no(node.filhos[i], title)

######################### IMPRIMIR ARVORE ########################
    def print_all(self):
        # Percorre e imprime todas as chaves da árvore B
        self._imprimir_todos_nos(self.raiz)

    def _imprimir_todos_nos(self, node):
        i = 0
        # Imprime as chaves dos nós em ordem
        for i in range(len(node.chaves)):
            # Primeiro, imprime as chaves do filho esquerdo, se houver
            if not node.folha:
                self._imprimir_todos_nos(node.filhos[i])
            # Em seguida, imprime a chave atual
            print(f"Título: {node.chaves[i]['title']}, Ano: {node.chaves[i]['year']}, Gênero: {node.chaves[i]['genre']}")
        
        # Finalmente, imprime o último filho, se existir
        if not node.folha:
            self._imprimir_todos_nos(node.filhos[i + 1])

######################## Função para salvar os dados em Excel ########################
    def percorrer(self):
        nos = []
        self._percorrer_recursivo(self.raiz, nos)
        return nos

    def _percorrer_recursivo(self, node, nos):
        if node.folha:
            nos.extend(node.chaves)
        else:
            for i, chave in enumerate(node.chaves):
                self._percorrer_recursivo(node.filhos[i], nos)
                nos.append(chave)
            self._percorrer_recursivo(node.filhos[-1], nos)


def save_to_excel(arvore_b, nome_arquivo="filmes.xlsx"):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["Título", "Ano", "Gênero"])  # Cabeçalho

    # Percorra os dados restantes na árvore e adicione-os ao arquivo Excel
    for filme in arvore_b.percorrer():
        sheet.append([filme["title"], filme["year"], filme["genre"]])

    workbook.save(nome_arquivo)
