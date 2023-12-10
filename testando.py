import time
import json
idNovo = 0
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

def cabecalho(texto):
    print("-"*40)
    print(texto.center(40))
    print("-"*40)

def cadastrarPacienteNovo():
    
    global idNovo 
    dadosGerais = {}
    arquivosJson = {}

    print("Opção 5 - Cadastrar novo paciente")
    cabecalho("CADASTRO DE NOVO PACIENTE")
    input_nome = str(input("Nome: "))

    while True:
        try:
            input_idade = int(input("Idade: "))
        except: 
            print("ERRO! Digite apenas números!")
        else:
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
            break
    
    paciente = Paciente(input_nome, input_idade, input_sexo, input_rg, input_cpf, idNovo)

    idNovo += 1
    
    print(paciente.nome)
    print(paciente.idade)
    print(paciente.sexo)
    print(paciente.rg)
    print(paciente.cpf)
    print(paciente.id)

    arquivosJson = {
        'nome': paciente.nome,
        'idade': paciente.idade,
        'sexo': paciente.sexo,
        'rg': paciente.rg,
        'cpf': paciente.cpf,
        'id': paciente.id
    }

    dadosGerais = {'id': paciente.id, 'dados': arquivosJson}

    try:
        with open('dadosPaciente.json', 'r') as arquivo:
            dadosPaciente = json.load(arquivo)

    except FileNotFoundError:
        dadosPaciente = {}
    
    dadosPaciente[idNovo] = arquivosJson

    #Criando o arquivo em json
    with open('dadosPaciente.json', 'w') as arquivo:
        json.dump(dadosPaciente, arquivo, indent=4)

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

while encerrarPrograma != True:
    cabecalho("MENU")
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
        cadastrarPacienteNovo()

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



