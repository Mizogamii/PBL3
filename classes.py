class Paciente():
    def __init__(self, nome, idade, sexo, rg, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf

class Recepcao():
    def __init__(self, dataSessao, horarioSessao): #, sessoes, fila
        self.dataSessao = dataSessao
        self.horarioSessao = horarioSessao
        """self.sessoes = sessoes
        self.fila = fila"""