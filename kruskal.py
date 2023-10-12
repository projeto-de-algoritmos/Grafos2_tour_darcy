from collections import defaultdict

class Grafo:

    def __init__(self, quantidadeNos) -> None:
        self.N = quantidadeNos # Quantidade de nós
        self.grafo = [] # Dicionário para armazenar o grafo

    def addAresta(self, id1, nome1, id2, nome2, pesoAresta):
        self.grafo.append([id1, nome1, id2, nome2, pesoAresta])
    
    

