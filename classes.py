class Paciente():
    def __init__(self, nome, idade, sexo, rg, cpf, id):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
        self.id = id

class Recepcao():
    def __init__(self, codigo, dataSessao, horarioSessao, duracaoSessao, tempoCadaConsulta, quantidadePacientePossivel):
        self.codigo = codigo
        self.dataSessao = dataSessao
        self.horarioSessao = horarioSessao
        self.duracaoSessao = duracaoSessao
        self.tempoCadaConsulta = tempoCadaConsulta
        self.quantidadePacientePossivel = quantidadePacientePossivel 

class MarcarHorarioPaciente():
    def __init__(self, ordemMarcacao, nomePaciente, dataMarcar, horarioMarcar):
        self.ordemMarcacao = ordemMarcacao
        self.nomePaciente = nomePaciente
        self.dataMarcar = dataMarcar
        self.horarioMarcar = horarioMarcar
    
        