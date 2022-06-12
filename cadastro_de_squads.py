class Pessoa:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone


class Squad:
    def __init__(self, nome, techlead=None, devs=None):
        self.nome = nome
        self.devs = []
        self.techlead = techlead

        def incluir_techlead(self, techlead):
            self.techlead = techlead