from datetime import datetime, time
import json
from classes import Paciente, Recepcao, MarcarHorarioPaciente

#Função para organizar os títulos
def cabecalho(texto):
    print("-"*47)
    print(texto.center(47))
    print("-"*47)

#Função para impressão do menu da recepção
def menuRecepcao():
    cabecalho("MENU RECEPÇÃO")
    print("""1 -  Adicionar nova sessão
2 -  Listar sessões clínicas 
3 -  Buscar sessão clínica
4 -  Iniciar sessão               
5 -  Cadastrar novo paciente
6 -  Marcar horário 
7 -  Listar horários marcados
8 -  Verificar se paciente tem horário marcado
9 -  Colocar paciente na fila de atendimento
10 - Mostrar próximo paciente na fila
11 - Listar consultas realizadas na sessão
12 - Sair do sistema """) 
    
    print("-"*47)

#Função para abrir o arquivo json para leitura
def abrirArquivo(nomeArquivo): 
    try:
        with open(nomeArquivo, 'r') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        dados = {}

    return dados

#Função para abrir o arquivo json para leitura, com diferença que nesse o except aparece uma mensagem
def abrirArquivoComMensagem(nomeArquivo, mensagem):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        dados = mensagem

    return dados

#Função para leitura de arquivos com o dicionário dentro de lista
def abrirArquivoLista(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivos:
            dadosLista = json.load(arquivos)
    except FileNotFoundError:
        dadosLista = []

    return dadosLista

#Função para a inserção dos dados no arquivo
def inserirDadosArquivo(nomeArquivo, dados):
    with open(nomeArquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

#Função para organizar id 
def codigoInicial(nomeArquivo, codigo):
    res = abrirArquivo(nomeArquivo) 
    #Verificando o último id inserido e acrescentando mais um para o próximo
    if res:
        ultimoId = max(map(int, res.keys()))
        codigo = ultimoId + 1
    else:
        codigo = 1

    return codigo

#Função para organizar os ids 
def inserindoId(dados, dicionario, codigo, id):
    idStr = str(id)

    #Adicionando o id ao dicionário
    dicionario[codigo] = id  

    #Adicionando o novo paciente com id
    dados[idStr] = dicionario

    return id

#Função da opção 1 de adicionar nova sessão clínica
def adicionarNovaSessao():
    permitido = True

    codigo = codigoInicial('dadosSessaoRecepcao.json', 'codigo')

    print("""Horário que inicia as sessões padrões: 
Sessão da manhã -- 08:00 
Sessão da tarde -- 14:00""")
    print("-"*47)
    print("Insira os dados pedidos: ")
    
    dataSessao = formatoData()
    horarioSessao = formatoHora()

    duracao = int(input("Duração dessa sessão, em horas: "))
    duracaoSessao = duracao * 60
    tempoCadaConsulta = int(input("Duração de cada consulta, em minutos: "))
    quantidadePacientePossivel = duracaoSessao // tempoCadaConsulta
    print("."*47)

    try: 
        with open('dadosSessaoRecepcao.json', 'r') as arquivos:
            dadosSessaoRecepcao = json.load(arquivos)
            for dados in dadosSessaoRecepcao.values():
                if dados['dataSessao'] == dataSessao and dados['horarioSessao'] == horarioSessao:
                    permitido = False
    except FileNotFoundError:
            dadosSessaoRecepcao = {}

    if permitido == True:
        #Inserindo as informações na classe
        recepcao = Recepcao(codigo, dataSessao, horarioSessao, duracaoSessao, tempoCadaConsulta, quantidadePacientePossivel)

        #Inserindo as informações em um dicionário
        arquivoRecepcaoNovo = {'codigo': recepcao.codigo,'dataSessao': recepcao.dataSessao,
                            'horarioSessao': recepcao.horarioSessao, 'duracaoSessao': duracaoSessao, 'tempoConsulta': tempoCadaConsulta, 'quantidadePacientePossivel': quantidadePacientePossivel}
        
        recepcao.codigo = inserindoId(dadosSessaoRecepcao, arquivoRecepcaoNovo, 'codigo', codigo)

        inserirDadosArquivo('dadosSessaoRecepcao.json', dadosSessaoRecepcao)
        
        print("Sessão adicionada com sucesso!")
    else:
        print("ERRO!\nJá existe uma sessão com essa data e horário.\nTente novamente!")

    return duracaoSessao, tempoCadaConsulta

#Função da opção 2 de listar as sessões clínicas
def listarSessao():
    dadosSessaoRecepcao = abrirArquivoComMensagem('dadosSessaoRecepcao.json', "ERRO! Não há dados a serem mostrados.")
    
    if dadosSessaoRecepcao:
        for codigo, dados in dadosSessaoRecepcao.items():
            print("Sessão: ", codigo)
            print("Data da sessão: ", dados['dataSessao'])
            print("Horário da sessão: ", dados['horarioSessao'])
            print("Quantidade de consultas possíveis: ", dados['quantidadePacientePossivel'])
            print("."*47)

#Função da opção 3 de buscar a sessão clínica
def buscarSessao():
    contadorSucessoBuscar = 0

    buscarData = formatoData()
    buscarHorario = formatoHora()

    print("."*47)

    try:
        with open('dadosSessaoRecepcao.json', 'r') as arquivos:
            dadosSessaoRecepcao = json.load(arquivos)
        
        for dados in dadosSessaoRecepcao.values():
            if dados['dataSessao'] == buscarData:
                if dados['horarioSessao'] == buscarHorario:
                    print("Sessão encontrada com sucesso.")
                    print("."*47)
                    print("Sessão número", dados['codigo'])
                    print("Data da sessão: ", dados['dataSessao'])
                    print("Duração de cada consulta: ", dados['tempoConsulta'], "minutos")
                    contadorSucessoBuscar = 1
        if contadorSucessoBuscar == 0:
            print("Não há sessões com essa data e horário.")

    except FileNotFoundError:
        print("ERRO! Não há dados a serem buscados.\nTente inicialmente executar a opção 1,\ninserindo dados.")

#Função da opção 4 de iniciar as sessões
def iniciarSessao():
    contadorTemHorario = 0
    #Abrindo arquivo para o armazenamento de dados essenciais das sessões 
    try: 
        with open('dadosSessaoRecepcao.json', 'r') as arquivos:
            dadosSessaoRecepcao = json.load(arquivos)

            dataSessaoIniciar = formatoData()
            horarioDaSessao = formatoHora()

            for dados in dadosSessaoRecepcao.values():
                if dataSessaoIniciar == dados['dataSessao'] and horarioDaSessao == dados['horarioSessao']:
                    print('Sessão aberta com sucesso.')
                    contadorTemHorario = 1
                    #Abrindo um arquivo para o armazenamento da data e horário da sessão aberta
                    dataHoraSessaoAberta = abrirArquivo('dataHoraSessaoAberta.json')

                    dataHoraSessaoAberta = {'data': dataSessaoIniciar, 'hora': horarioDaSessao}

                    inserirDadosArquivo('dataHoraSessaoAberta.json', dataHoraSessaoAberta)

    except FileNotFoundError:
        print("ERRO! Arquivo da recepção não encontrado!\nTente inserir os dados na opção 1.")

    if contadorTemHorario == 0: 
        print("Não há sessões com essa data e horário\ncadastrados no sistema.")

#Função da opção 5 de adicionar novo paciente (cadastro)
def cadastrarPaciente():

    id = codigoInicial('dadosPaciente.json', 'id')

    input_nome = str(input("Nome: ")).upper()

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

    #dadosGerais = {'id': id, 'dados': arquivosJson}

    dadosPaciente = abrirArquivo('dadosPaciente.json')
    paciente.id = inserindoId(dadosPaciente, arquivosJson, 'id', id)
    inserirDadosArquivo('dadosPaciente.json', dadosPaciente)

    print(f"\nCliente adicionado com sucesso! ID: {paciente.id}")

#Função da opção 6 de marcar horário para paciente
def marcarHorario():
    contadorNomeCerto = 0
    sucessoMarcar = 0
    contadorDataHoraIguais = 0
    deuErro = 0
    repetido = False
    
    ordemMarcacao = codigoInicial('horariosMarcadosRecepcao.json', 'ordemMarcacao')

    #Abrindo o arquivo de cadastramento de clientes para verificação da existência de cadastro
    try: 
        with open('dadosPaciente.json', 'r') as arquivo:
            dadosPaciente = json.load(arquivo)

        #Pedindo o nome do paciente
        nomePaciente = input("Informe o nome do paciente: ").upper()

        #Verificando se o nome existe no arquivo de cadastro
        for dados in dadosPaciente.values():
            if dados['nome'] == nomePaciente:
                contadorNomeCerto = 1
        
        if contadorNomeCerto == 0: 
            print("Não há cadastros com este nome!\nTente novamente!")

        #Pedindo a data e horário que o paciente deseja marcar 
        else: 
            dataMarcar = formatoData()
            horarioMarcar = formatoHora()

            print("."*47)

            #Abrindo arquivo de horários marcados para inserir os dados
            try:
                with open('horariosMarcadosRecepcao.json', 'r') as arquivos:
                    horariosMarcadosRecepcao = json.load(arquivos)

                    for dados in horariosMarcadosRecepcao.values():
                        if dados['data'] == dataMarcar and dados['horario'] == horarioMarcar:
                            contadorDataHoraIguais += 1
                    print(f"Contador iguais: {contadorDataHoraIguais}")
                    
                    #Verificar se o paciente tem um horário marcado para não marcar duas vezes
                    for informacoes in horariosMarcadosRecepcao.values():
                        if informacoes['nomePac'] == nomePaciente and informacoes['data'] == dataMarcar and informacoes['horario'] == horarioMarcar:
                            repetido = True
                            print("Paciente já está com horário marcado.")
            except FileNotFoundError:
                horariosMarcadosRecepcao = {}
        
            try:
                with open('dadosSessaoRecepcao.json', 'r') as arquivos:
                    dadosSessaoRecepcao = json.load(arquivos)

                for dados in dadosSessaoRecepcao.values():
                    if dados['dataSessao'] == dataMarcar and dados['horarioSessao'] == horarioMarcar:
                        if dados['quantidadePacientePossivel'] > contadorDataHoraIguais and repetido == False: 
                            print("Horário marcado com sucesso.")
                            sucessoMarcar = 1

                            marcando = MarcarHorarioPaciente(ordemMarcacao, nomePaciente, dataMarcar, horarioMarcar)
                             
                            marcarHorarioSessao = {'ordemMarcacao': marcando.ordemMarcacao ,'nomePac': marcando.nomePaciente, 'data': marcando.dataMarcar, 'horario': marcando.horarioMarcar}
                            
                            marcando.ordemMarcacao = inserindoId(horariosMarcadosRecepcao, marcarHorarioSessao, 'ordemMarcacao', ordemMarcacao)
                            
                            inserirDadosArquivo('horariosMarcadosRecepcao.json', horariosMarcadosRecepcao)
                        else: 
                            deuErro = 1
                            if repetido == False:
                                print("Não há mais vagas nessa sessão.\nTente em um outro horário ou data.") 

                if sucessoMarcar == 0 and deuErro == 0:
                    print("Não há sessões para essa data e horário.\nTente novamente com novos dados.")

            except FileNotFoundError:
                print("ERRO! Não há dados a serem mostrados.")

    except FileNotFoundError:
        print("Arquivo da recepção não encontrada!\nTente inicialmente inserir os dados nas \nopções 1 e 5.")

#Função da opção 7 de listar os horários marcados do paciente  
def listarHorariosMarcados():
    contadorNomeCerto = 0
    try: 
        with open('horariosMarcadosRecepcao.json', 'r') as arquivo:
            horariosMarcadosRecepcao = json.load(arquivo)
        
        nomePaciente = input("Informe o nome do paciente: ").upper()
        
        for dados in horariosMarcadosRecepcao.values():
            if dados['nomePac'] == nomePaciente:
                contadorNomeCerto = 1
                print("."*47)
                print(f"Nome: {dados['nomePac']}")
                print(f"Data: {dados['data']}")
                print(f"Horário: {dados['horario']}")
        
        if contadorNomeCerto == 0: 
            print("Não há reservas para este nome.\nTente novamente!")

    except FileNotFoundError:
        print("Arquivo da recepção não encontrada!\nTente inicialmente inserir os dados.\nPara isso utilize as opções 1, 5 e 6. ")  

#Função da opção 8 de confirmar se paciente está com horário marcado 
def confirmarHorario():
    situacaoDaSessao = sessaoAbertaOuFechada()
    if situacaoDaSessao == True:
        nomePaciente = input("Informe o nome do paciente: ").upper()

        nomeConsta = verificacaoPacienteMarcado(nomePaciente)

        if nomeConsta == 1:
            print("Paciente está com horário marcado.")
        else:
            print("Não há horários marcados para esse paciente")
    else: 
        print("Não há sessões abertas no momento.\nTente novamente.")
        
#Função da opção 9 de colocar o paciente na lista de atendimento
def colocarNaListaAtendimento():
    situacaoDaSessao = sessaoAbertaOuFechada()
    if situacaoDaSessao == True:
        nomePaciente = input("Informe o nome do paciente: ").upper()
        verificacao = verificacaoPacienteMarcado(nomePaciente)
        if verificacao == 1:
            listaDeAtendimentoPacientes(nomePaciente)
        else:
            print("Não há horário marcado com esse nome.\nVerifique se não há erros na escrita e\ntente novamente.")
    else: 
        print("Não há sessões abertas no momento.\nTente novamente.")

#Função da opção 10 de mostrar aos paciente e dentistas a próxima pessoa a ser atendida
def listarProximos():
    try:
        with open('listaDeAtendimento.json', 'r') as arquivos:
            pacientesMarcadosSessao = json.load(arquivos)
            if pacientesMarcadosSessao:
                print(pacientesMarcadosSessao[0]['nome'])
            else:
                print("Não há mais pacientes na fila")

    except FileNotFoundError:
        print("ERRO! Não há dados no arquivo!\nTente inicialmente abrir a sessão ou verificar\nse algum paciente tem um horário marcado nessa\nsessão. Para isso, utilize a opção 8.")

#Função da opção 11 de mostrar todas as consultas realizadas na sessão
def listarConsultasRealizadas():
    try:
        with open('listaPacientesAtendidos.json', 'r') as arquivos:
            listaPacientesAtendidos = json.load(arquivos)
            for dados in listaPacientesAtendidos:
                print("Nome: ", dados['nome'])
                print("Data: ", dados['data'])
                print("Horário: ", dados['hora'])
                print("."*47)

    except FileNotFoundError:
        print("ERRO! Ainda não foram atendidos pacientes nessa sessão.")
    
#Função para formatação das datas
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

#Função para formatação das horas
def formatoHora():
    while True:
        try:
            inputHora = input("Hora da sessão [hh:mm]: ")
            hora = datetime.strptime(inputHora, "%H:%M").time()
            hora = hora.strftime("%H:%M")
        except ValueError:
            print("ERRO! Digite no formato pedido.")
        
        else:
            break
    return hora

#Função para listar os pacientes que estão marcados na sessão aberta no sistema
def pacientesComHoraMarcadaSessao():
    try:
        with open('dataHoraSessaoAberta.json', 'r') as arquivo:
            dataHoraSessaoAberta = json.load(arquivo)

            dataSessaoAberta = dataHoraSessaoAberta['data']
            horaSessaoAberta = dataHoraSessaoAberta['hora']
            
            horariosMarcadosRecepcao = abrirArquivo('horariosMarcadosRecepcao.json')

            #Leitura dos pacientes que estão marcados para a sessão aberta para poder fazer a verificação                
            pacientesMarcadosSessao = abrirArquivoLista('pacientesMarcadosSessao.json')

            #Inserindo os dados do paciente na lista de atendimento
            for dados in horariosMarcadosRecepcao.values():
                if dataSessaoAberta == dados['data'] and horaSessaoAberta == dados['horario']:
                    pacientesAtual = {
                        'nome': dados['nomePac'], 
                        'data': dados['data'], 
                        'horario': dados['horario']
                    }

                if pacientesAtual not in pacientesMarcadosSessao:
                    pacientesMarcadosSessao.append(pacientesAtual)
                    
                    inserirDadosArquivo('pacientesMarcadosSessao.json', pacientesMarcadosSessao)

    except FileNotFoundError:
        print("ERRO! Tente iniciar a sessão na opção 4.")

#Função para verificar se há ou não uma sessão aberta 
def sessaoAbertaOuFechada():
    aberta = False
    try:
        with open('dataHoraSessaoAberta.json', 'r') as arquivos:
            dataHoraSessaoAberta = json.load(arquivos)
            if dataHoraSessaoAberta != {}:
                aberta = True
            else:
                dataHoraSessaoAberta = {}
    except FileNotFoundError:
        dataHoraSessaoAberta = {}
    
    with open('dataHoraSessaoAberta.json', 'w') as arquivos:
        json.dump(dataHoraSessaoAberta, arquivos, indent=4)

    return aberta

#Função para listar os pacientes que apareceram para a consulta da sessão que foi iniciado 
def listaDeAtendimentoPacientes(nomePaciente):
    ordemPacientesMarcados = abrirArquivoLista('pacientesMarcadosSessao.json')
    print(nomePaciente)
    
    listaDeAtendimento = abrirArquivoLista('listaDeAtendimento.json')

    paciente = None

    for dados in ordemPacientesMarcados:
        if nomePaciente == dados['nome']:
            paciente = {
                'nome': dados['nome'],
                'data': dados['data'],
                'hora': dados['horario'],
                'paciente': "presente"
            }

        if paciente not in listaDeAtendimento and paciente is not None:
            listaDeAtendimento.append(paciente)
        
            inserirDadosArquivo('listaDeAtendimento.json', listaDeAtendimento)

#Verificação se paciente está com horário marcado
def verificacaoPacienteMarcado(nomePaciente):
    nomeConsta = 0
    pacientesComHoraMarcadaSessao() #É listado nessa função todos os pacientes que estão com horário marcado para a sessão atual
    try:
        with open('pacientesMarcadosSessao.json', 'r') as arquivos:
            pacientesMarcadosSessao = json.load(arquivos)
    
        for dados in pacientesMarcadosSessao:
            if dados['nome'] == nomePaciente:
                nomeConsta = 1

    except FileNotFoundError:
        print("Não há dados no arquivo!")
    
    return nomeConsta

#FUNÇÕES DA PARTE DO DENTISTA
#Função para impressão do menu do dentista
def menuDentista():
    cabecalho("MENU DENTISTA")
    print("""1 - Buscar sessão clínica
2 - Iniciar sessão clínica
3 - Atender próximo paciente
4 - Ler prontuário de paciente
5 - Ler a primeira anotação do paciente
6 - Ler a última anotação do paciente
7 - Anotar no prontuário
8 - Sair do sistema""")
    print("-"*47)

#Função da opção 3 para atender o próximo paciente da lista
def atenderProxPaciente():
    filaVazia = True
    try:
        with open('listaDeAtendimento.json', 'r') as arquivos:
            listaDeAtendimento = json.load(arquivos)
            if listaDeAtendimento != []:
                print("Nome: ", listaDeAtendimento[0]['nome'])
                print("Data: ", listaDeAtendimento[0]['data'])
                print("Horário: ", listaDeAtendimento[0]['hora'])
                print("."*47)
                filaVazia = False
                nomeDoPacienteEmAtendimento = listaDeAtendimento[0]['nome']
                
                #Apagando o paciente já atendido do arquivo de pessoas comhorário marcado
                horariosMarcRecepcao = abrirArquivo("horariosMarcadosRecepcao")
                if horariosMarcRecepcao:
                    elementoExcluir = []
                    for elementos, dados in horariosMarcRecepcao.items():
                        if dados['nomePac'] == nomeDoPacienteEmAtendimento:
                            elementoExcluir.append(elementos)
                            
                    for elementos in elementoExcluir:
                        del horariosMarcRecepcao[elementos]
                        
                    inserirDadosArquivo("horariosMarcadosRecepcao", horariosMarcRecepcao) 
                     
                listaPacientesAtendidos = abrirArquivoLista('listaPacientesAtendidos.json')
                        
                pacienteAtendidoAtual = {'nome': listaDeAtendimento[0]['nome'], 'data': listaDeAtendimento[0]['data'], 'hora': listaDeAtendimento[0]['hora']}

                listaPacientesAtendidos.append(pacienteAtendidoAtual)

                inserirDadosArquivo('listaPacientesAtendidos.json', listaPacientesAtendidos)

                del listaDeAtendimento[0]

                inserirDadosArquivo('listaDeAtendimento.json', listaDeAtendimento)
        
            else:
                print("Não há mais pacientes na fila.\nSESSÃO ENCERRADA COM SUCESSO!")
                filaVazia = True
                try:
                    with open('dataHoraSessaoAberta.json', 'r') as arquivo:
                        conteudoArquivo = arquivo.read()
                        if conteudoArquivo:
                            arquivo.close()
                            encerrar = input("Deseja encerrar sessão? [S/N]: ").upper()
                            if encerrar == "S":
                                print("Sessão finalizada!")
                                try:
                                    with open('dataHoraSessaoAberta.json', 'r') as arquivos:
                                        dataHoraSessaoAberta = json.load(arquivos)
                                        if dataHoraSessaoAberta:
                                            del dataHoraSessaoAberta['data']
                                            del dataHoraSessaoAberta['hora']
                                        
                                        inserirDadosArquivo('dataHoraSessaoAberta.json',dataHoraSessaoAberta)
                                    with open("pacientesMarcadosSessao.json", 'w') as arquivo:
                                        pass

                                except FileNotFoundError:
                                    print("ERRO! Arquivo não encontrado.")   
                                
                except FileNotFoundError:
                    print("ERRO!")
            
    except FileNotFoundError:
        print("Erro! Não há pacientes na fila.")

    if filaVazia == False:
        return nomeDoPacienteEmAtendimento
    else:
        return None

#Função da opção 4 para ler o prontuário do paciente que está sendo atendido
def lerProntuario(nomePacienteAtendido):
    print(nomePacienteAtendido)

#Função da opção 5 para ler a primeira anotação feita na consulta do paciente
def lerPrimeiraAnotacao():
    pass

#Função da opção 6 para ler a anotação da última vez que o paciente esteve na consulta
def lerUltimaAnotacao():
    pass

#Função da opção 7 para anotar informações do paciente no prontuário
def anotarProntuario():
    pass