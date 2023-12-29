class Paciente():
    def __init__(self, nome, idade, sexo, rg, cpf, id):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
        self.id = id

class Recepcao():
    def __init__(self, codigo, dataSessao, horarioSessao):
        self.codigo = codigo
        self.dataSessao = dataSessao
        self.horarioSessao = horarioSessao

class MarcarHorario():
    def __init__(self, nome, dataMarcar, horarioMarcar):
        self.nome = nome
        self.dataMarcar = dataMarcar
        self.horarioMarcar = horarioMarcar
        