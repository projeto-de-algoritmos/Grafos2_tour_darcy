class Grafo:

    def __init__(self, quantidadeNos) -> None:
        self.N = quantidadeNos # Quantidade de nós
        self.grafo = [] # Dicionário para armazenar o grafo

    def addAresta(self, id1, nome1, id2, nome2, pesoAresta):
        self.grafo.append([id1, nome1, id2, nome2, pesoAresta])
    
    # Retorna a raiz de um Nó do unionFind
    def procura(self, raizes, id):
        if raizes[id] == id:
            return id
        return self.procura(raizes, raizes[id])
    
    # Faz a união das árvores do unionFind
    def uniao(self, raizes, altura, x, y):
        xRaiz = self.procura(raizes, x)
        yRaiz = self.procura(raizes, y)

        # Coloca a árvore com menor altura na que tiver maior
        if altura[xRaiz] < altura[yRaiz]:
            raizes[xRaiz] = yRaiz
        elif altura[xRaiz] > altura[yRaiz]:
            raizes[yRaiz] = xRaiz

        # Se forem iguais, uma fica embaixo da outra e tem que aumentar a altura
        else:
            raizes[yRaiz] = xRaiz
            altura[xRaiz] += 1
    
    def kruskal(self):

        resultado = [] #irá armazenar as arestas que formam a árvore mínima
        total = 0; #irá armazenar o total da soma dos pesos das arestas

        i = 0 # index para iteração das arestas

        e = 0 # index usada para resultado[]

        # Primeiro passo: Ordenar arestas por peso
        self.grafo = sorted(self.grafo, key= lambda item: item[4])

        raizes = [] #variável para armazenar a coluna de raiz da UnionFind
        altura = [] #variável para armazenar a altura de cada raiz da UnionFind

        for no in range(self.N): #Inicializar cada nó do UnionFind
            raizes.append(no)
            altura.append(0) # Todo nó começa com altura 0


        while e < self.N - 1:

            # Segundo passo: pegar a menor aresta e incrementar o index para próxima iteração
            id1, nome1, id2, nome2, pesoAresta = self.grafo[i]
            i += 1
            x = self.procura(raizes, id1)
            y = self.procura(raizes, id2)

            # Se incluir essa aresta não for fomar um ciclo, adiciona em resultado
            if x!=y:
                e += 1
                resultado.append([id1, nome1, id2, nome2, pesoAresta])
                total += pesoAresta
                self.uniao(raizes, altura, x, y)
            # Se não, descarta a aresta

        print("A seguinte é a árvore mínima construída")
        print(f"Total: {total} ")
        for id1, nome1, id2, nome2, pesoAresta in resultado:
            print(nome1 + " - " + nome2 + f": {pesoAresta}")