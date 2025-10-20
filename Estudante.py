class Estudante:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas  # lista com 4 notas (floats)

    def calcularMedia(self):
        return sum(self.notas) / len(self.notas)