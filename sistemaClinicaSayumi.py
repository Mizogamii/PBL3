class cadastro():
    def __init__(self, nome, idade, sexo, rg, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
        self.id = 0

def cabecalho(texto):
    print("-"*40)
    print(texto.center(40))
    print("-"*40)
          
class prontuario(cadastro):
    def __init__(self, nome, idade, sexo, rg, cpf):
        super().__init__(nome, idade, sexo, rg, cpf)

    def imprimir(self):
        cabecalho("PRONTUÁRIO")
        print(f"""Paciente: {self.nome}
Idade: {self.idade}
Sexo: {self.sexo}
RG: {self.rg}
CPF: {self.cpf}  
""")


        