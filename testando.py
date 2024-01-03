from datetime import datetime
import json
from classes import Paciente, Recepcao, MarcarHorarioPaciente

#Função para organizar os títulos
def cabecalho(texto):
    print("-"*40)
    print(texto.center(40))
    print("-"*40)

#Função para impressão do menu 
def menu():
    cabecalho("MENU")
    print("""1 - Adicionar nova sessão
2 - Listar sessões clínicas 
3 - Buscar sessão clínica
4 - Iniciar sessão      
5 - Cadastrar novo paciente
6 - Marcar horário 
7 - Buscar paciente
8 - Listar próximos pacientes
9 - Sair do sistema """)
    print("-"*40)

def salvarArquivo(nomeArquivo, arq, numero):
#Abrindo o arquivo para leitura
    try:
        with open(nomeArquivo, 'r') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        dados = {}

    #Procurando o último id para conseguir botar o próximo com a numeração certa
    if dados:
        ultimoId = max(map(int, dados.keys()))
        ultimoId = int(ultimoId)
        id = ultimoId + 1
    else:
        id = 1

    id_str = str(id)
    arq[numero] = id
    dados[str(id)] = arq

    # Adicionando o novo paciente com id
    dados[id_str] = arq

    # Inserção dos dados no arquivo
    with open(nomeArquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    return id
    
#Função da opção 1 de adicionar nova sessão clínica
def adicionarNovaSessao():
    codigo = 0
    print("Opção 1 - Adicionar nova sessão")
    cabecalho("ADICIONAR NOVA SESSÃO")
    print("""Horário que inicia as sessões padrões: 
Sessão 1 -- 08:00 
Sessão 2 -- 14:00""")
    print("-"*40)
    print("Insira os dados pedidos: ")
    
    dataSessao = formatoData()

    horarioSessao = int(input("Horário da nova sessão: "))
    duracao = int(input("Duração dessa sessão, em horas: "))
    duracaoSessao = duracao * 60
    tempoCadaConsulta = int(input("Duração de cada consulta, em minutos: "))
    quantidadePacientePossivel = duracaoSessao // tempoCadaConsulta
    
    #Inserindo as informações na classe
    recepcao = Recepcao(codigo, dataSessao, horarioSessao, duracaoSessao, tempoCadaConsulta, quantidadePacientePossivel)

    #Inserindo as informações em um dicionário
    arquivoRecepcaoNovo = {'codigo': recepcao.codigo,'dataSessao': recepcao.dataSessao,
                        'horarioSessao': recepcao.horarioSessao, 'duracaoSessao': duracaoSessao, 'tempoConsulta': tempoCadaConsulta, 'quantidadePacientePossivel': quantidadePacientePossivel}
    
    recepcao.codigo = salvarArquivo('dadosSessaoRecepcao.json', arquivoRecepcaoNovo, 'codigo')

    #Só para testes
    print(recepcao.codigo)
    print(recepcao.dataSessao)
    print(recepcao.horarioSessao) 
    print(recepcao.tempoCadaConsulta)
    print(recepcao.duracaoSessao)

    print("\nSessão adicionada com sucesso!")

    return duracaoSessao, tempoCadaConsulta

#Função da opção 3 de buscar a sessão clínica
def buscarSessao():
    cabecalho("BUSCAR SESSÃO")
    buscarData = formatoData()
    buscarHorario = int(input("Informe o horário a ser buscado: "))
    print("."*40)

    try:
        with open('dadosSessaoRecepcao.json', 'r') as arquivos:
            dadosSessaoRecepcao = json.load(arquivos)
        
        for dados in dadosSessaoRecepcao.values():
            if dados['dataSessao'] == buscarData:
                if dados['horarioSessao'] == buscarHorario:
                    print("Sessão encontrada com sucesso.\n")
                    print("Sessão número", dados['codigo'])
                    contadorSucessoBuscar = 1

        if contadorSucessoBuscar == 0:
            print("Não há sessões com essa data e horário.")

    except FileNotFoundError:
        print("ERRO! Não há dados a serem buscados.\nTente inicialmente executar a opção 1,\ninserindo dados.")

def listarSessao():
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
            print("Quantidade de consultas possíveis: ", dados['quantidadePacientePossivel'])
            print("."*40)

def iniciarSessao():
    pass

#Função da opção 5 de adicionar novo paciente (cadastro)
def cadastrarPaciente():
    id = 0
    cabecalho("CADASTRO DE NOVO PACIENTE")

    input_nome = str(input("Nome: "))

    #Tratamento de dados, só aceita números
    while True:
        try:
            input_idade = int(input("Idade: "))
        except ValueError: 
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

    id = salvarArquivo('dadosPaciente.json', arquivosJson, 'id')

    print(f"\nCliente adicionado com sucesso! ID: {id}")

#Função da opção 6 de marcar horário para paciente
def marcarHorario():
    contadorNomeCerto = 0
    sucessoMarcar = 0
    contadorDataHoraIguais = 0
    cabecalho("MARCAR HORÁRIO")
    try: 
        with open('dadosPaciente.json', 'r') as arquivo:
            dadosPaciente = json.load(arquivo)
        
        nomePaciente = input("Informe o nome do paciente: ")
        for dados in dadosPaciente.values():
            if dados['nome'] == nomePaciente:
                contadorNomeCerto = 1
        
        if contadorNomeCerto == 0: 
            print("Não há cadastros com este nome!\nTente novamente!")
            
        else: 
            dataMarcar = formatoData()
            horarioMarcar = int(input("Insira o horário da sessão desejada: "))
            print("."*40)
    
            try:
                with open('horariosMarcadosRecepcao.json', 'r') as arquivos:
                    horariosMarcadosRecepcao = json.load(arquivos)
                    for dados in horariosMarcadosRecepcao.values():
                        if dados['data'] == dataMarcar and dados['horario'] == horarioMarcar:
                            contadorDataHoraIguais += 1
                    print(f"Contador iguais: {contadorDataHoraIguais}")

            except FileNotFoundError:
                horariosMarcadosRecepcao = {}
        
            try:
                with open('dadosSessaoRecepcao.json', 'r') as arquivos:
                    dadosSessaoRecepcao = json.load(arquivos)

                for dados in dadosSessaoRecepcao.values():
                    if dados['dataSessao'] == dataMarcar and dados['horarioSessao'] == horarioMarcar:
                        if dados['quantidadePacientePossivel'] > contadorDataHoraIguais: 
                            print("Horário marcado com sucesso.")
                            sucessoMarcar = 1

                            marcando = MarcarHorarioPaciente(nomePaciente, dataMarcar, horarioMarcar)
                            
                            marcarHorarioSessao = {'nomePac': marcando.nomePaciente, 'data': marcando.dataMarcar, 'horario': marcando.horarioMarcar}

                            contador = salvarArquivo('horariosMarcadosRecepcao.json', marcarHorarioSessao, 'ordemMarcacao')
                        else: 
                            print("Não há mais vagas nessa sessão.\nTente em um outro horário ou data.")

                if sucessoMarcar == 0:
                    print("Não há sessões para essa data e horário.\nTente novamente com novos dados.")

            except FileNotFoundError:
                print("ERRO! Não há dados a serem mostrados.")

    except FileNotFoundError:
        print("Arquivo da recepção não encontrada!\nTente inicialmente inserir os dados nas \nopções 1 e 5.")

def buscarPaciente():
    contadorNomeCerto = 0
    try: 
        with open('horariosMarcadosRecepcao.json', 'r') as arquivo:
            horariosMarcadosRecepcao = json.load(arquivo)
        
        nomePaciente = input("Informe o nome do paciente: ")
        print("."*40)
        #print(f"Todos os horários marcados pelo paciente \n{nomePaciente} ")
        
        for dados in horariosMarcadosRecepcao.values():
            if dados['nomePac'] == nomePaciente:
                contadorNomeCerto = 1
                print("."*40)
                print(f"Nome: {dados['nomePac']}")
                print(f"Data: {dados['data']}")
                print(f"Horário: {dados['horario']}")
        
        if contadorNomeCerto == 0: 
            print("Não há reservas para este nome.\nTente novamente!")

    except FileNotFoundError:
        print("Arquivo da recepção não encontrada!\nTente inicialmente inserir os dados nas \nopções 1 e 5.") 

def listarProximos():
    pass

def formatoData():
    while True:
        try:
            inputDataSessao = input("Data da sessão[dd/mm/yyyy]: ")
            data = datetime.strptime(inputDataSessao, "%d/%m/%Y")
        
            if data < datetime.now():
                print("Digite anos atuais!")
                continue

            data = data.strftime("%d/%m/%Y")
        except ValueError: 
            print("ERRO! Digite no formato pedido.")
        else:
            break
    return data

encerrarPrograma = False
dadosGerais = {}
arquivosJson = {}
cont = 0

while encerrarPrograma != True:
    if cont == 0:
        menu()
    else: 
        resposta = input("Aperte ENTER para continuar")
        print('\033c', end='')
        menu()

    cont += 1

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
        adicionarNovaSessao()
        
    elif opcao == 2: 
        print("Opção 2 - Listar sessões clínicas")
        listarSessao()

    elif opcao == 3: 
        print("Opção 3 - Buscar sessão")
        buscarSessao()
    
    elif opcao == 4:
        print("Opção 4 - Iniciar sessão")
        
    elif opcao == 5:
        print("Opção 5 - Cadastrar novo paciente")
        cadastrarPaciente()
        
    elif opcao == 6:
        print("Opção 6 - Marcar horário")
        marcarHorario()
        
    elif opcao == 7:
        print("Opção 7 - Buscar paciente")
        cabecalho("BUSCAR PACIENTE")
        buscarPaciente()


    elif opcao == 8:
        print("Opção 8 - Listar próximos pacientes")
    
    elif opcao == 9:
        print("\nEncerrando...")
        encerrarPrograma = True
    
    print("-"*40)



