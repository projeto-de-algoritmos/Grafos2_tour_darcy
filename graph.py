from array import array

class Link:
    def __init__(self, nome, pos, distancia) -> None:
        self.nome = nome
        self.pos = pos
        self.distancia = distancia

class Predio:
    def __init__(self, id, nome, links: list ) -> None:
        self.id = id
        self.nome = nome
        self.links = links

darcy = array("P", [
    Predio(2, "Faculdade de Medicina / Faculdade de Ciências da Saúde", []),
    Predio(3, "Faculdade de Direito", []),
    Predio(4, "Faculdade de Administração, Contabilidade e Economia", []),
    Predio(5, "Faculdade de Tecnologia", []),
    Predio(6, "Faculdade de Educação Física", []),
    Predio(7, "Faculdade de Educação", []),
    Predio(8, "Instituto de Química", []),
    Predio(9, "Instituto de Ciências Biológicas", []),
    Predio(10, "Pavilhão Multiuso I", []),
    Predio(11, "Pavilhão Multiuso II", []),
    Predio(12, "Laboratório de Engenharia Mecânica", []),
    Predio(13, "Laboratório de Engenharia Elétrica", []),
    Predio(14, "Laboratório de Engenharia Civil", []),
    Predio(15, "Oficinas Especiais - Instituto de Artes", []),
    Predio(16, "Instituto de Artes", []),
    Predio(17, "Departamento de Música", []),
    Predio(18, "Auditório de Música", []),
    Predio(19, "Departamento de Música", []),
    Predio(21, "Restaurante Universitário", []),
    Predio(22, "Instituto Central de Ciências", []),
    Predio(23, "Reitoria", []),
    Predio(24, "Biblioteca Central", []),
])