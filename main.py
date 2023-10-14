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
# ICC, id = 23
# Memorial Darcy Ribeiro, id = 24
# Reitoria, id = 25
# BCE, id = 26
# Centro Comunitário Athos Bulcão, id = 27
# CIC/EST, id = 28
# FD, id = 29
# FACE, id = 30
# PAT, id = 31
# PJC, id = 32
# IPOL/IREL, id = 33
# BAES, id = 34
# BSAN, id = 35
# ICS, id = 36
# CEU Bloco K, id = 37
# FEF, id = 38
# CO, id = 39
# CEU Bloco B, id = 40
# CEU Bloco A, id = 41

g = Grafo(42)
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
g.addAresta(17, "Restaurante Universitário", 23, "ICC", 0.24)
g.addAresta(8, "IB", 23, "ICC", 1.7)
g.addAresta(8, "IB", 24, "Memorial Darcy Ribeiro", 1.7)
g.addAresta(23, "ICC", 24, "Memorial Darcy Ribeiro", 0.65)
g.addAresta(23, "ICC", 25, "Reitoria", 0.6)
g.addAresta(23, "ICC", 26, "BCE", 0.7)
g.addAresta(24, "Memorial Darcy Ribeiro", 25, "Reitoria", 0.074)
g.addAresta(25, "Reitoria", 26, "BCE", 0.55)
g.addAresta(26, "BCE", 27, "Centro Comunitário Athos Bulcão", 0.9)
g.addAresta(26, "BCE", 28, "CIC/EST", 0.95)
g.addAresta(28, "CIC/EST", 27, "Centro Comunitário Athos Bulcão", 0.5)
g.addAresta(28, "CIC/EST", 33, "IPOL/IREL", 0.078)
g.addAresta(33, "IPOL/IREL", 27, "Centro Comunitário Athos Bulcão", 0.4)
g.addAresta(28, "CIC/EST", 32, "PJC", 0.26)
g.addAresta(32, "PJC", 33, "IPOL/IREL", 0.21)
g.addAresta(33, "IPOL/IREL", 34, "BAES", 0.29)
g.addAresta(34, "BAES", 32, "PJC", 0.3)
g.addAresta(32, "PJC", 31, "PAT", 0.089)
g.addAresta(32, "PJC", 30, "FACE", 0.11)
g.addAresta(32, "PJC", 35, "BSAN", 0.22)
g.addAresta(31, "PAT", 30, "FACE", 0.2)
g.addAresta(30, "FACE", 35, "BSAN", 0.18)
g.addAresta(29, "FD", 28, "CIC/EST", 0.4)
g.addAresta(29, "FD", 31, "PAT", 0.27)
g.addAresta(29, "FD", 30, "FACE", 0.25)
g.addAresta(29, "FD", 21, "CCN", 0.22)
g.addAresta(29, "FD", 19, "EFL", 0.35)
g.addAresta(27, "Centro Comunitário Athos Bulcão", 34, "BAES", 0.3)
g.addAresta(34, "BAES", 35, "BSAN", 0.26)
g.addAresta(35, "BSAN", 36, "ICS", 0.35)
g.addAresta(36, "ICS", 30, "FACE", 0.4)
g.addAresta(36, "ICS", 29, "FD", 0.3)
g.addAresta(37, "CEU Bloco K", 21, "CCN", 0.6)
g.addAresta(37, "CEU Bloco K", 22, "PRC", 0.65)
g.addAresta(37, "CEU Bloco K", 36, "ICS", 0.35)
g.addAresta(38, "FEF", 24, "Memorial Darcy Ribeiro", 1.1)
g.addAresta(38, "FEF", 8, "IB", 2)
g.addAresta(38, "FEF", 41, "CEU Bloco A", 0.3)
g.addAresta(41, "CEU Bloco A", 40, "CEU Bloco B", 0.35)
g.addAresta(41, "CEU Bloco A", 39, "CO", 1.6)
g.addAresta(40, "CEU Bloco B", 39, "CO", 1.4)
g.addAresta(38, "FEF", 39, "CO", 1.9)

g.kruskal()