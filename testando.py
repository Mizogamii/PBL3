import time
import json
from classes import Paciente, Recepcao, MarcarHorario

#Função para organizar os títulos
def cabecalho(texto):
    print("-"*40)
    print(texto.center(40))
    print("-"*40)

def salvarArquivo(nomeArquivo, arq):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        dados = {}

    if dados:
        ultimoId = max(map(int, dados.keys()))
        ultimoId = int(ultimoId)
        id = ultimoId + 1
    else:
        id = 1

    id_str = str(id)
    arq['id'] = id
    dados[str(id)] = arq
    # Adiciona o novo paciente
    dados[id_str] = arq

    # Salvando os dados no arquivo
    with open(nomeArquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    return id
    


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
dadosGerais = {}
arquivosJson = {}
id = 0
codigo = 0

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
        contadorSucessoBuscar = 0
        sucessoMarcar = 0

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
        cabecalho("ADICIONAR NOVA SESSÃO")
        print("""Horário que inicia as sessões padrões: 
Sessão 1 -- 08:00 
Sessão 2 -- 14:00""")
        print("-"*40)
        
        dataSessao = int(input("Insira a data da nova sessão: "))
        horarioSessao = int(input("Insira o horário da nova sessão: "))

        #Inserindo as informações na classe
        recepcao = Recepcao(codigo, dataSessao, horarioSessao)

        #Inserindo as informações em um dicionário
        arquivoRecepcaoNovo = {'codigo': recepcao.codigo,'dataSessao': recepcao.dataSessao,
                           'horarioSessao': recepcao.horarioSessao}
        
        #Só para testes
        print(recepcao.codigo)
        print(recepcao.dataSessao)
        print(recepcao.horarioSessao)   

        #Abrindo o arquivo para inserir as informações/verificando se já existe o arquivo
        try:
            with open('dadosSessaoRecepcao.json', 'r') as arquivos:
                dadosSessaoRecepcao = json.load(arquivos)

        except FileNotFoundError:
            dadosSessaoRecepcao = {}
        
        if dadosSessaoRecepcao:
            ultimoCodigo = max(map(int, dadosSessaoRecepcao.keys()))
            recepcao.codigo = ultimoCodigo + 1
        else:
            recepcao.codigo = 1

        codigoStr = str(recepcao.codigo)
        arquivoRecepcaoNovo['codigo'] = recepcao.codigo
        dadosSessaoRecepcao[str(recepcao.codigo)] = arquivoRecepcaoNovo

        # Adiciona o nova sessão
        dadosSessaoRecepcao[codigoStr] = arquivoRecepcaoNovo

        # Salva os dados no arquivo
        with open('dadosSessaoRecepcao.json', 'w') as arquivos:
            json.dump(dadosSessaoRecepcao, arquivos, indent=4)

        print(f"Sessão adicionada com sucesso!")

    elif opcao == 2: 
        print("Opção 2 - Listar sessões clínicas")
        cabecalho("LISTAR SESSÕES CLÍNICAS")
        try:
            with open('dadosSessaoRecepcao.json', 'r') as arquivos:
                dadosSessaoRecepcao = json.load(arquivos)

        except FileNotFoundError:
            print("ERRO! Não há dados a serem mostrados.")
        
        if dadosSessaoRecepcao:
            for codigo, dados in dadosSessaoRecepcao.items():
                print("Sessão: ", codigo)
                print("Data da sessão: ", dados['dataSessao'])
                print("Horário da sessão: ", dados['horarioSessao'])
                print("."*40)


    elif opcao == 3: 
        print("Opção 3 - Buscar sessão")
        cabecalho("BUSCAR SESSÃO")
        buscarData = int(input("Informe a data a ser buscada: "))
        buscarHorario = int(input("Informe o horário a ser buscado: "))
        print("."*40)

        try:
            with open('dadosSessaoRecepcao.json', 'r') as arquivos:
                dadosSessaoRecepcao = json.load(arquivos)
            
            for elementos, dados in dadosSessaoRecepcao.items():
                if dados['dataSessao'] == buscarData:
                    if dados['horarioSessao'] == buscarHorario:
                        print("Sessão encontrada com sucesso.\n")
                        print("Sessão número", dados['codigo'])
                        contadorSucessoBuscar = 1

            if contadorSucessoBuscar == 0:
                print("Não há sessões com essa data e horário.")

        except FileNotFoundError:
            print("ERRO! Não há dados a serem buscados.\nTente inicialmente executar a opção 1,\ninserindo dados.")
    
    elif opcao == 4:
        print("Opção 4 - Iniciar sessão")
        
    elif opcao == 5:
        print("Opção 5 - Cadastrar novo paciente")
        cabecalho("CADASTRO DE NOVO PACIENTE")

        input_nome = str(input("Nome: "))

        #Tratamento de dados, só aceita números
        while True:
            try:
                input_idade = int(input("Idade: "))
            except: 
                print("ERRO! Digite apenas números!")
            else:
                break

        #Tratamento de dados, somente aceita F ou M, feminino ou masculino
        while True:
            try:
                input_sexo = str(input("Sexo[M/F]: ")).upper()
                if input_sexo != "M" and input_sexo != "F":
                    print("ERRO! Digite apenas M ou F!")
                    continue
            except ValueError:
                print("ERRO! Digite apenas M ou F!")
            else:
                break

        #Tratamento de dados, como é rg somente aceita 10 dígitos
        while True:
            try:
                input_rg = int(input("RG: "))
                if len(str(input_rg)) != 10:
                    print("ERRO! Digite somente os 10 números do RG")
                    continue
            except ValueError:
                print("ERRO! Digite apenas números!")
            else:
                break

        #Tratamento de dados, como é cpf somente aceita 11 dígitos     
        while True:
            try:
                input_cpf = int(input("CPF: "))
                if len(str(input_cpf)) != 11:
                    print("ERRO! Digite somente os 11 números do CPF")
                    continue
            except ValueError:
                print("ERRO! Digite apenas números!")
            else:
                break

        #Inserindo as informações na classe
        paciente = Paciente(input_nome, input_idade, input_sexo, input_rg, input_cpf, id)

        #Inserindo os dados dentro do dicionário
        arquivosJson = {
            'nome': paciente.nome,
            'idade': paciente.idade,
            'sexo': paciente.sexo,
            'rg': paciente.rg,
            'cpf': paciente.cpf,
            'id': paciente.id
        }

        dadosGerais = {'id': id, 'dados': arquivosJson}

        id = salvarArquivo('dadosPaciente.json', arquivosJson)

        print(f"Cliente adicionado com sucesso! ID: {id}")

    elif opcao == 6:
        print("Opção 6 - Marcar horário")
        cabecalho("MARCAR HORÁRIO")
        nomePaciente = input("Informe o nome do paciente: ")
        horarioMarcar = int(input("Insira o horário da sessão desejada: "))
        dataMarcar = int(input("Insira a data da sessão desejada: "))

        try:
            with open('dadosSessaoRecepcao.json', 'r') as arquivos:
                dadosSessaoRecepcao = json.load(arquivos)

            for elementos, dados in dadosSessaoRecepcao.items():
                if dados['dataSessao'] == dataMarcar:
                    if dados['horarioSessao'] == horarioMarcar:
                        print("Horário marcado com sucesso.")
                        sucessoMarcar = 1

                        marcarHorario = (nomePaciente, dataMarcar, horarioMarcar)

                        marcarHorarioSessao = {'nomePac': nomePaciente, 'data': dataMarcar, 'horario': horarioMarcar}

                        contador = salvarArquivo('horariosMarcadosRecepcao.json', marcarHorarioSessao )
                    
            if sucessoMarcar == 0:
                print("Não há sessões para essa data e horário.\nTente novamente com novos dados.")


        except FileNotFoundError:
            print("ERRO! Não há dados a serem mostrados.")
        
    
    elif opcao == 7:
        print("Opção 7 - Buscar paciente")

    elif opcao == 8:
        print("Opção 8 - Listar próximos pacientes")
    
    elif opcao == 9:
        print("Encerrando...")
        encerrarPrograma = True

    """time.sleep(2) #Só para teste
    print('\033c', end='')"""



