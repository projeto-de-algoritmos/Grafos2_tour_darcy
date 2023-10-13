from kruskal import Grafo

# CAEP, id = 0
# CET, id = 1
# CDS, id = 2
# Pavilhão Multiuso II, id = 3
# Faculdade de educação, id = 4
# BSAS, id = 5
# FM/FS, id = 6
# IQ, id = 7
# IB, id = 8
# SG9, id = 9
# SG11, id = 10
# SG12, id = 11
# Oficinas Especiais, id = 12
# Pavilhão Multiuso I, id = 13
# Instituto de Artes, id = 14
# Departamento de Música, id = 15
# Auditório de Música, id = 16
# Restaurante Universitário, id = 17
# Faculdade de Tecnologia, id = 18
# EFL, id = 19
# Uleg-FT, id = 20
# CCN, id = 21
# PRC, id = 22

g = Grafo(23)
g.addAresta(0, "CAEP", 1, "CET", 0.75)
g.addAresta(1, "CET", 2, "CDS", 0.13)
g.addAresta(2, "CDS", 3, "Pavilhão Multiuso II", 0.25)
g.addAresta(1, "CET", 4, "Faculdade de educação", 0.28)
g.addAresta(0, "CAEP", 3, "Pavilhão Multiuso II", 0.6)
g.addAresta(3, "Pavilhão Multiuso II", 5, "BSAS", 0.9)
g.addAresta(5, "BSAS", 6, "FM/FS", 0.75)
g.addAresta(6, "FM/FS", 7, "IQ", 0.6)
g.addAresta(7, "IQ", 8, "IB", 0.4)
g.addAresta(5, "BSAS", 8, "IB", 0.043)
g.addAresta(4, "Faculdade de educação", 9, "SG9", 0.24)
g.addAresta(9, "SG9", 10, "SG11", 0.09)
g.addAresta(10, "SG11", 11, "SG12", 0.097)
g.addAresta(9, "SG9", 12, "Oficinas Especiais", 0.034)
g.addAresta(4, "Faculdade de educação", 12, "Oficinas Especiais", 0.35)
g.addAresta(3, "Pavilhão Multiuso II", 13, "Pavilhão Multiuso I", 0.4)
g.addAresta(12, "Oficinas Especiais", 14, "Instituto de Artes", 0.29)
g.addAresta(13, "Pavilhão Multiuso I", 14, "Instituto de Artes", 0.2)
g.addAresta(9, "SG9", 15, "Departamento de Música", 0.15)
g.addAresta(10, "SG11", 15, "Departamento de Música", 0.061)
g.addAresta(11, "SG12", 15, "Departamento de Música", 0.16)
g.addAresta(15, "Departamento de Música", 16, "Auditório de Música", 0.28)
g.addAresta(11, "SG12", 16, "Auditório de Música", 0.12)
g.addAresta(16, "Auditório de Música", 17, "Restaurante Universitário", 0.35)
g.addAresta(14, "Instituto de Artes", 17, "Restaurante Universitário", 0.4)
g.addAresta(16, "Auditório de Música", 18, "Faculdade de Tecnologia", 0.17)
g.addAresta(18, "Faculdade de Tecnologia", 19, "EFL", 0.24)
g.addAresta(19, "EFL", 20, "Uleg-FT", 0.35)
g.addAresta(19, "EFL", 21, "CCN", 0.28)
g.addAresta(21, "CCN", 22, "PRC", 0.2)
g.addAresta(20, "Uleg-FT", 22, "PRC", 0.24)

g.kruskal()