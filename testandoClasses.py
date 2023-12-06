import time
class Paciente():
    def __init__(self, nome, idade, sexo, rg, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
        #self.id = id
        
    def cadastrarNovoPaciente(self, nome, idade, sexo, rg, cpf, dicionario):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
        dicionario = {'nome': nome, 'idade': idade, 'sexo': sexo, 'rg': rg, 'cpf': cpf}

    def cabecalho(texto):
        print("-"*40)
        print(texto.center(40))
        print("-"*40)

    def adicionarNovaSessao():
        pass

    def buscarSessao():
        pass

    def iniciarSessao():
        pass

    def marcarHorario():
        pass

    def buscarPaciente():
        pass

    def listarProximos():
        pass

encerrarPrograma = False
dicionario = dict
dadosPaciente = {}


while encerrarPrograma != True:
    Paciente.cabecalho("MENU")
    print("""1 - Adicionar nova sessão
2 - Listar sessões clínicas 
3 - Buscar sessão
4 - Iniciar sessão      
5 - Cadastrar novo paciente
6 - Marcar horário 
7 - Buscar paciente
8 - Listar próximos pacientes
9 - Sair do sistema """)
    print("-"*40)

    while True:
        try:
            opcao = int(input("Opcão escolhida: "))
        except:
            print("ERRO! Digite apenas números de 1 a 9!")
        else:
            if opcao <= 9:
                break
            else:
                print("ERRO! Digite apenas de 1 a 9!")
                continue

    if opcao == 1:
        print("Opção 1 - Adicionar nova sessão")

    elif opcao == 2: 
        print("Opção 2 - Listar sessões clínicas")

    elif opcao == 3: 
        print("Opção 3 - Buscar sessão")

    elif opcao == 4:
        print("Opção 4 - Iniciar sessão")
        
    elif opcao == 5:
        print("Opção 5 - Cadastrar novo paciente")
        Paciente.cabecalho("CADASTRO DE NOVO PACIENTE")
        input_nome = str(input("Nome: "))
        dadosPaciente["nome"] = input_nome

        while True:
            try:
                input_idade = int(input("Idade: "))
            except: 
                print("ERRO! Digite apenas números!")
            else:
                dadosPaciente["idade"] = input_idade
                break

        while True:
            try:
                input_sexo = str(input("Sexo[M/F]: ")).upper()
                if input_sexo != "M" and input_sexo != "F":
                    print("ERRO! Digite apenas M ou F!")
                    continue
            except:
                print("ERRO! Digite apenas M ou F!")
            else:
                dadosPaciente["sexo"] = input_sexo
                break
        
        while True:
            try:
                input_rg = int(input("RG: "))
                if len(str(input_rg)) != 10:
                    print("ERRO! Digite somente os 10 números do RG")
                    continue
            except:
                print("ERRO! Digite apenas números!")
            else:
                dadosPaciente["rg"] = input_rg
                break

        while True:
            try:
                input_cpf = int(input("CPF: "))
                if len(str(input_cpf)) != 11:
                    print("ERRO! Digite somente os 11 números do CPF")
                    continue
            except:
                print("ERRO! Digite apenas números!")
            else:
                dadosPaciente["cpf"] = input_cpf
                break

        print(dadosPaciente)
        paciente = Paciente(input_nome, input_idade, input_sexo, input_rg, input_cpf)

        print(paciente.nome)
        print(paciente.idade)
        print(paciente.sexo)
        print(paciente.rg)
        print(paciente.cpf)

    elif opcao == 6:
        print("Opção 6 - Buscar paciente")
    
    elif opcao == 7:
        print("Opção 7 - Marcar horário")

    elif opcao == 8:
        print("Opção 8 - Listar próximos pacientes")
    
    elif opcao == 9:
        encerrarPrograma = True

    """time.sleep(2) #Só para teste
    print('\033c', end='')"""



