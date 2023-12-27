class Paciente():
    def __init__(self, nome, idade, sexo, rg, cpf, id):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
        self.id = id

class Recepcao():
    def __init__(self, data, horario, sessoes, fila):
        self.data = data
        self.horario = horario
        self.sessoes = sessoes
        self.fila = fila