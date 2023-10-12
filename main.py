from kruskal import Grafo

g = Grafo(4)
g.addAresta(0, "Predio0", 1, "Predio1", 10)
g.addAresta(0, "Predio0", 2, "Predio2", 6)
g.addAresta(0, "Predio0", 3, "Predio3", 5)
g.addAresta(1, "Predio1", 3, "Predio3", 15)
g.addAresta(2, "Predio2", 3, "Predio3", 4)

g.kruskal()