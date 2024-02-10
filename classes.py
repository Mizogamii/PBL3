"""Autor: Sayumi Mizogami Santana
Componente Curricular: EXA 854 - MI - Algoritmos
Concluído em: 21/02/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação."""

#Sistema operacional utilizado: Windows
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
    
        