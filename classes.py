class Paciente():
    def __init__(self, nome, idade, sexo, rg, cpf, id):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
        self.id = id

class Recepcao():
    def __init__(self, codigo, dataSessao, horarioSessao, duracaoSessao, tempoCadaConsulta):
        self.codigo = codigo
        self.dataSessao = dataSessao
        self.horarioSessao = horarioSessao
        self.duracaoSessao = duracaoSessao
        self.tempoCadaConsulta = tempoCadaConsulta

class MarcarHorarioPaciente():
    def __init__(self, nome, dataMarcar, horarioMarcar):
        self.nome = nome
        self.dataMarcar = dataMarcar
        self.horarioMarcar = horarioMarcar
    
        