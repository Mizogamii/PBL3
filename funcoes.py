"""Autor: Sayumi Mizogami Santana
Componente Curricular: EXA 854 - MI - Algoritmos
Concluído em: 21/02/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação."""

#Sistema operacional utilizado: Windows
#Existe um with open com path na linha 703

from datetime import datetime
import json
from classes import Paciente, Recepcao, MarcarHorarioPaciente
from pathlib import Path

#Função para organizar os títulos
def cabecalho(texto):
    print("-"*47)
    print(texto.center(47))
    print("-"*47)

#Função para realizar o login do dentista ou da recepção
def login():
    entradaValida = False
    cabecalho("USUÁRIO")
    print("1 - Recepção\n2 - Dentista\n3 - Sair")
    print("."*47)

    #Tratamento de dados, o usuário só poderá digitar números de 1 a 3
    while not entradaValida:
        try:
            usuario = int(input("Informe a sua opção: "))
            if 0 < usuario <= 3:
                entradaValida = True
            else:
                print("ERRO! Digite apenas 1 ou 3.")
                continue
        except ValueError:
            print("ERRO! Digite apenas números(1 ou 3)")
    print()
    return usuario

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
12 - Sair da página da recepção """) 
    
    print("-"*47)

#Função para abrir o arquivo json para leitura com dicionário dentro de dicionário
def abrirArquivo(nomeArquivo):
    caminho = salvarEmPasta(nomeArquivo)

    try:
        with caminho.open('r') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        dados = {}

    return dados

#Função para abrir o arquivo json para leitura, com diferença que nesse o except aparece uma mensagem
def abrirArquivoComMensagem(nomeArquivo, mensagem):
    caminho = salvarEmPasta(nomeArquivo)
    dados = None

    try:
        with caminho.open('r') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        print(mensagem)

    if dados:
        return dados
    
#Função para leitura de arquivos com o dicionário dentro de lista
def abrirArquivoLista(nomeArquivo):
    caminho = salvarEmPasta(nomeArquivo)

    try:
        with caminho.open('r') as arquivos:
            dadosLista = json.load(arquivos)
    except FileNotFoundError:
        dadosLista = []

    return dadosLista

#Função para a inserção dos dados no arquivo
def inserirDadosArquivo(nomeArquivo, dados):
    caminho = salvarEmPasta(nomeArquivo)
    # Salvando os dados no arquivo JSON no novo caminho
    with caminho.open('w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def salvarEmPasta(nomeArquivo):
    # Definindo o caminho da pasta onde os arquivos JSON serão salvos
    pastaArquivos = Path('pastaComArquivos')

    # Verifica se a pasta existe, se não, cria a pasta
    pastaArquivos.mkdir(exist_ok=True)
    
    # Cria o caminho completo do arquivo incluindo a pasta 'dados'
    caminho = pastaArquivos / nomeArquivo

    return caminho

#Função para fazer id 
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

    codigo = codigoInicial('dadosSessaoRecepcao.json', 'codigo') #Chamando a função para fazer o id da sessão

    print("""Horário que inicia as sessões padrões: 
Sessão da manhã -- 08:00 
Sessão da tarde -- 14:00""")
    print("-"*47)
    print("Insira os dados pedidos: ")

    #Funções para a inserção de datas e horários nos formatos corretos 
    dataSessao = formatoData()
    horarioSessao = formatoHora()

    duracao = tratamentoDados("Duração dessa sessão, em horas: ")

    duracaoSessao = duracao * 60

    tempoCadaConsulta = tratamentoDados("Duração de cada consulta, em minutos: ")

    quantidadePacientePossivel = duracaoSessao // tempoCadaConsulta
    print("."*47)
    dadosSessaoRecepcao = abrirArquivo('dadosSessaoRecepcao.json')
    
    for dados in dadosSessaoRecepcao.values():
        #Verificando se não há datas e horários repetidos e assim permitir a inserção dos dados no arquivo 
        if dados['dataSessao'] == dataSessao and dados['horarioSessao'] == horarioSessao: 
            permitido = False

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
    #Chamando função para abrir o arquivo
    dadosSessaoRecepcao = abrirArquivoComMensagem('dadosSessaoRecepcao.json', "ERRO! Não há dados a serem mostrados.")
    #Imprimindo dados das sessões cadastrados
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
    #Abrindo arquivo de sessões para a verificação da existência da sessão nos dados cadastrados
    dadosSessaoRecepcao = abrirArquivoComMensagem('dadosSessaoRecepcao.json', "ERRO! Não há dados a serem buscados.\nTente inicialmente executar a opção 1, inserin-\ndo dados." ) 
    if dadosSessaoRecepcao:
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

#Função da opção 4 de iniciar as sessões
def iniciarSessao():
    contadorTemHorario = 0
    #Abrindo arquivo para o armazenamento de dados essenciais das sessões 

    dadosSessaoRecepcao = abrirArquivoComMensagem('dadosSessaoRecepcao.json', "ERRO! Arquivo da recepção não encontrado!\nTente inserir os dados na opção 1." )
    
    if dadosSessaoRecepcao:
        dataSessaoIniciar = formatoData()
        horarioDaSessao = formatoHora()

        for dados in dadosSessaoRecepcao.values():
            if dataSessaoIniciar == dados['dataSessao'] and horarioDaSessao == dados['horarioSessao']:
                print('Sessão aberta com sucesso.')
                contadorTemHorario = 1

                #Abrindo um arquivo para o armazenamento da data e horário da sessão aberta
                dataHoraSessaoAberta = abrirArquivo('dataHoraSessaoAberta.json')

                dataHoraSessaoAberta = {'data': dataSessaoIniciar, 'hora': horarioDaSessao, 'sessaoAbertaConsulta': "Fechada", 'situacao': True}

                inserirDadosArquivo('dataHoraSessaoAberta.json', dataHoraSessaoAberta)

        if contadorTemHorario == 0: 
            print("Não há sessões com essa data e horário cadas-\ntrados no sistema.")

#Função da opção 5 de adicionar novo paciente (cadastro)
def cadastrarPaciente():
    dadosValidos = False

    id = codigoInicial('dadosPaciente.json', 'id')

    input_nome = str(input("Nome: ")).upper()

    #Tratamento de dados, só aceita números
    while not dadosValidos:
        try:
            input_idade = int(input("Idade: "))
        except ValueError: 
            print("ERRO! Digite apenas números!")
        else:
            dadosValidos = True

    #Tratamento de dados, somente aceita F ou M, feminino ou masculino
    dadosValidos = False
    while not dadosValidos:
        try:
            input_sexo = str(input("Sexo[M/F]: ")).upper()
            if input_sexo == "M" or input_sexo == "F":
                dadosValidos = True
            else:
                print("ERRO! Digite apenas M ou F!")
                
        except ValueError:
            print("ERRO! Digite apenas M ou F!")

    #Tratamento de dados, como é RG somente aceita 10 dígitos
    dadosValidos = False
    while not dadosValidos:
        try:
            input_rg = int(input("RG: "))
            if len(str(input_rg)) == 10:
                dadosValidos = True
            else: 
                print("ERRO! Digite somente os 10 números do RG")

        except ValueError:
            print("ERRO! Digite apenas números!")
    

    #Tratamento de dados, como é cpf somente aceita 11 dígitos     
    dadosValidos = False
    while not dadosValidos:
        try:
            input_cpf = int(input("CPF: "))
            if len(str(input_cpf)) == 11:
                dadosValidos = True
            else:
                print("ERRO! Digite somente os 11 números do CPF")
                
        except ValueError:
            print("ERRO! Digite apenas números!")

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
    #Inserindo dados dentro do arquivo json para armazenamento dos dados do paciente
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

    #Abrindo o arquivo de cadastramento de clientes para verificação da existência de cadastro, caso não exista dados não será permitido marcar horário

    dadosPaciente = abrirArquivoComMensagem('dadosPaciente.json', "Arquivo da recepção não encontrada!\nTente inicialmente inserir os dados nas \nopções 1 e 5." )

    if dadosPaciente:
        #Pedindo o nome do paciente
        nomePaciente = input("Informe o nome do paciente: ").upper()

        #Verificando se o nome existe no arquivo de cadastro
        for dados in dadosPaciente.values():
            if dados['nome'] == nomePaciente:
                contadorNomeCerto = 1

        if contadorNomeCerto == 0: 
            print("Não há cadastros com este nome!\nTente novamente!")

        #Pedindo a data e horário que o paciente deseja marcar caso haja dados do paciente cadastrados no sistema
        else: 
            dataMarcar = formatoData()
            horarioMarcar = formatoHora()

            print("."*47)

            #Abrindo arquivo de horários marcados para inserir os dados
            horariosMarcadosRecepcao = abrirArquivo('horariosMarcadosRecepcao.json')
            
            for dados in horariosMarcadosRecepcao.values():
                if dados['data'] == dataMarcar and dados['horario'] == horarioMarcar:
                    contadorDataHoraIguais += 1
            
            #Verificar se o paciente tem um horário marcado para não marcar duas vezes
            for informacoes in horariosMarcadosRecepcao.values():
                if informacoes['nomePac'] == nomePaciente and informacoes['data'] == dataMarcar and informacoes['horario'] == horarioMarcar:
                    repetido = True
                    print("Paciente já está com horário marcado.")

            #Abrindo o arquivo com os dados da recepção sobre as sessões cadastradas no sistema para verificação
            dadosSessaoRecepcao = abrirArquivoComMensagem('dadosSessaoRecepcao.json', "ERRO! Não há dados a serem mostrados.")
            
            #Verificação da possibilidade de marcar um horário, é necessário ainda ter vagas para consultas e também a existência da sessão que foi escolhido pelo paciente no sistema
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

#Função da opção 7 de listar os horários marcados do paciente  
def listarHorariosMarcados():
    contadorNomeCerto = 0
    horariosMarcadosRecepcao = abrirArquivoComMensagem('horariosMarcadosRecepcao.json', "Arquivo da recepção não encontrada!\nTente inicialmente inserir os dados.\nPara isso utilize as opções 1, 5 e 6. ")

    if horariosMarcadosRecepcao:
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

#Função da opção 8 de confirmar se paciente está com horário marcado 
def confirmarHorario():
    situacaoDaSessao = sessaoAbertaOuFechada()
    if situacaoDaSessao == True:
        nomePaciente = input("Informe o nome do paciente: ").upper()

        nomeConsta = verificacaoPacienteMarcado(nomePaciente)

        if nomeConsta == 1:
            print("Paciente está com horário marcado.")
        else:
            print("Não há horários marcados para esse paciente.")
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
            print("Não há horário marcado com esse nome.\nVerifique se não há erros na escrita e tente\nnovamente.")

    else: 
        print("Não há sessões abertas momento.\nTente novamente.")

#Função da opção 10 de mostrar aos paciente e dentistas a próxima pessoa a ser atendida
def listarProximos():
    pacientesMarcadosSessao = abrirArquivoComMensagem('listaDeAtendimento.json', "ERRO! Não há dados no arquivo!\nTente inicialmente abrir a sessão ou inserir um\npaciente na fila de atendimento.\nPara isso, utilize a opção 9.")
        
    if pacientesMarcadosSessao:
        print(pacientesMarcadosSessao[0]['nome'])
    else:
        print("Não há pacientes na fila")

#Função da opção 11 de mostrar todas as consultas realizadas na sessão
def listarConsultasRealizadas():
    listaPacientesAtendidos = abrirArquivoComMensagem('listaPacientesAtendidos.json',"ERRO! Ainda não foram atendidos pacientes nessa\nsessão." )

    if listaPacientesAtendidos:
        for dados in listaPacientesAtendidos:
            print("Nome: ", dados['nome'])
            print("Data: ", dados['data'])
            print("Horário: ", dados['hora'])
            print("."*47)
    
#Função para formatação das datas
def formatoData():
    entradaValida = False
    while not entradaValida:
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
            entradaValida = True
    return data

#Função para tratar os dados inseridos pelo usuário
def tratamentoDados(mensagem):
    entradaValida = False
    while not entradaValida:
        try:
            dados = int(input(mensagem))
        except ValueError: 
            print("ERRO! Digite apenas números!")
        else:
            entradaValida = True
    return dados

#Função para formatação das horas
def formatoHora():
    entradaValida = False
    while not entradaValida:
        try:
            inputHora = input("Hora da sessão [hh:mm]: ")
            hora = datetime.strptime(inputHora, "%H:%M").time()
            hora = hora.strftime("%H:%M")
        except ValueError:
            print("ERRO! Digite no formato pedido.")
        
        else:
            entradaValida = True
    return hora

#Função para listar os pacientes que estão marcados na sessão aberta no sistema
def pacientesComHoraMarcadaSessao():
    dataHoraSessaoAberta = abrirArquivoComMensagem('dataHoraSessaoAberta.json', "ERRO! Tente iniciar a sessão na opção 4.")

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

#Função para verificar se há ou não uma sessão aberta 
def sessaoAbertaOuFechada():
    aberta = False

    dataHoraSessaoAberta = abrirArquivo('dataHoraSessaoAberta.json')
    
    if dataHoraSessaoAberta != {}:
        aberta = True
    else:
        dataHoraSessaoAberta = {}
    
    inserirDadosArquivo('dataHoraSessaoAberta.json', dataHoraSessaoAberta)

    return aberta

#Função para listar os pacientes que apareceram para a consulta da sessão que foi iniciado 
def listaDeAtendimentoPacientes(nomePaciente):
    ordemPacientesMarcados = abrirArquivoLista('pacientesMarcadosSessao.json')
    
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
    
    print("Paciente na lista: ", nomePaciente)

#Verificação se paciente está com horário marcado
def verificacaoPacienteMarcado(nomePaciente):
    nomeConsta = 0
    pacientesComHoraMarcadaSessao() #É listado nessa função todos os pacientes que estão com horário marcado para a sessão atual
    pacientesMarcadosSessao = abrirArquivoComMensagem('pacientesMarcadosSessao.json', "Não há dados no arquivo!")
    if pacientesMarcadosSessao:
        for dados in pacientesMarcadosSessao:
            if dados['nome'] == nomePaciente:
                nomeConsta = 1
        
        return nomeConsta

#-----------------------------------------------------------------------------------
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
8 - Sair da página do dentista""")
    print("-"*47)

#Função da opção 2 para abrir uma sessão para iniciar as consultas
def abrirSessaoConsulta():
    sessaoAbertaConsulta = False
    sessao = sessaoAbertaOuFechada()

    if sessao: 
        print("Sucesso em iniciar a sessão para consulta.")
        sessaoAbertaConsulta = True
        dataHora = abrirArquivo('dataHoraSessaoAberta.json')
        
        data = dataHora['data']
        hora = dataHora['hora']

        dadosGerais = {'data': data, 'hora': hora, 'sessaoAbertaConsulta': "Aberta", 'situacao': True}
        
        inserirDadosArquivo('dataHoraSessaoAberta.json', dadosGerais)

    else: 
        print("Não há sessões iniciadas pela recepção.\nContate a recepção e tente novamente.")
    
    return sessaoAbertaConsulta

#Função da opção 3 para atender o próximo paciente da lista
def atenderProxPaciente():
    filaVazia = True
    #Abrindo arquivo da lista de atendimento para atender o próximo da fila
    listaDeAtendimento = abrirArquivoComMensagem('listaDeAtendimento.json', "Erro! Não há pacientes na fila.")

    if listaDeAtendimento != [] and listaDeAtendimento != None:
        #Imprimindo dados do paciente em atendimento
        print("Nome: ", listaDeAtendimento[0]['nome'])
        print("Data: ", listaDeAtendimento[0]['data'])
        print("Horário: ", listaDeAtendimento[0]['hora'])
        print("."*47)

        filaVazia = False #Enquanto houver pessoas na fila ficará em false

        nomeDoPacienteEmAtendimento = listaDeAtendimento[0]['nome']

        #Abrindo arquivo com a lista de pacientes atendidos para poder mostrar depois na opção 11 da recepção     
        listaPacientesAtendidos = abrirArquivoLista('listaPacientesAtendidos.json')
        
        #Inserindo dados no dicionário para ser deletado da fila após o atendimento
        pacienteAtendidoAtual = {'nome': listaDeAtendimento[0]['nome'], 'data': listaDeAtendimento[0]['data'], 'hora': listaDeAtendimento[0]['hora']}

        listaPacientesAtendidos.append(pacienteAtendidoAtual)

        inserirDadosArquivo('listaPacientesAtendidos.json', listaPacientesAtendidos)

        del listaDeAtendimento[0] #Tirando o paciente já atendido da lista de atendimento

        inserirDadosArquivo('listaDeAtendimento.json', listaDeAtendimento)
        
        #Armazenando em variáveis a data e o horário da sessão que está aberta no momento para possíveis verificações
        datasHoraSessao = abrirArquivo("dataHoraSessaoAberta.json")
        
        data = datasHoraSessao['data']
        hora = datasHoraSessao['hora']
        
        #Apagando o paciente já atendido do arquivo de pessoas com horário marcado
        deletarHorario = []
        pacientesHorario = abrirArquivo("horariosMarcadosRecepcao.json")
        for elemento, dados in pacientesHorario.items():
            if nomeDoPacienteEmAtendimento == dados['nomePac'] and data == dados['data'] and hora == dados['horario']:
                deletarHorario.append(elemento)

        for dados in deletarHorario:
            del pacientesHorario[dados]
        inserirDadosArquivo("horariosMarcadosRecepcao.json", pacientesHorario)

    #Para caso não haja mais pacientes na fila de atendimento
    else:
        print("Não há mais pacientes na fila.")
        filaVazia = True
        situacaoSessao = sessaoAbertaOuFechada() #Chamando a função que verifica se tem alguma sessão aberta no momento para poder deletar informações da sessão encerrada

        if situacaoSessao == True:
            caminho = salvarEmPasta('dataHoraSessaoAberta.json')

            try:
                with caminho.open('r') as arquivo:
                    conteudoArquivo = arquivo.read()
                    if conteudoArquivo:
                        arquivo.close()
                        #Perguntando ao usuário se deseja encerrar a sessão para poder apagar os dados
                        encerrar = input("Deseja encerrar sessão? [S/N]: ").upper()
                        if encerrar == "S":
                            print("Sessão finalizada!")

                            #Apagando data, horário e situação da sessão aberta do arquivo 
                            dataHoraSessaoAberta = abrirArquivoComMensagem('dataHoraSessaoAberta.json', "ERRO! Arquivo não encontrado.")
                            data = dataHoraSessaoAberta['data']
                            hora = dataHoraSessaoAberta['hora']

                            if dataHoraSessaoAberta:
                                del dataHoraSessaoAberta['data']
                                del dataHoraSessaoAberta['hora']
                                del dataHoraSessaoAberta['sessaoAbertaConsulta']
                                del dataHoraSessaoAberta['situacao']

                                #Limpando a sessão encerrada da lista de sessões
                                deletarSessao = []

                                sessao = abrirArquivo("dadosSessaoRecepcao.json")

                                for elemento, dados in sessao.items():
                                    if  data == dados['dataSessao'] and hora == dados['horarioSessao']:
                                        deletarSessao.append(elemento)

                                for dados in deletarSessao:
                                    del sessao[dados]
                                inserirDadosArquivo("dadosSessaoRecepcao.json", sessao)
                        
                            #Salvando dados no arquivo da data e horário da sessão aberta
                            inserirDadosArquivo('dataHoraSessaoAberta.json',dataHoraSessaoAberta) 

                            #Limpando o arquivo que armazenava os dados dos pacientes que tinham hora marcada na sessão aberta
                            pacientesMarcadosSessao = abrirArquivoLista("pacientesMarcadosSessao.json")
                            pacientesMarcadosSessao.clear()
                            inserirDadosArquivo("pacientesMarcadosSessao.json", pacientesMarcadosSessao)

                            #Limpando o arquivo que armazenava os dados dos pacientes que foram atendidos na sessão aberta, já que agora a sessão já foi realizada e encerrada.
                            listaAtendidosSessao = abrirArquivoLista("listaPacientesAtendidos.json")
                            listaAtendidosSessao.clear()
                            inserirDadosArquivo("listaPacientesAtendidos.json",listaAtendidosSessao)

                        else:
                            dataHoraSessaoAberta = abrirArquivo('dataHoraSessaoAberta.json')
                            dataHoraSessaoAberta['situacao'] = False
                            inserirDadosArquivo('dataHoraSessaoAberta.json',dataHoraSessaoAberta)
                    
            except FileNotFoundError:
                print("ERRO!")

    if filaVazia == False:
        return nomeDoPacienteEmAtendimento
    else:
        return None

#Função da opção 4 para ler o prontuário do paciente que está sendo atendido
def lerProntuario(nomePacienteAtendido):
    if nomePacienteAtendido != None:
        dadosPaciente = abrirArquivo("dadosPaciente.json")
        for dados in dadosPaciente.values():
            if dados['nome'] == nomePacienteAtendido:
                print(f"""Nome: {dados['nome']}
Idade: {dados['idade']}
Sexo: {dados['sexo']}
RG: {dados['rg']}
CPF: {dados['cpf']}""")
        dataHora = abrirArquivo("dataHoraSessaoAberta.json")
        if dataHora:
            print("Data do atendimento: ", dataHora['data'])
            print("Horário da sessão: ", dataHora['hora'])
    else: 
        print("Não há pacientes em atendimento no momento.")

#Função da opção 5 para ler a primeira anotação feita na consulta do paciente
def lerPrimeiraAnotacao(nomePacienteAtendido):
    if nomePacienteAtendido != None:
        anotacoesGerais = listaDeAnotacoes(nomePacienteAtendido)
        if anotacoesGerais != []:
            print("Paciente: ", nomePacienteAtendido)
            print("Alergias: ", anotacoesGerais[0]['alergia'])
            print("Motivo da consulta: ", anotacoesGerais[0]['queixa'])
            print("Data do atendimento: ", anotacoesGerais[0]['data'])
            print("Horário da sessão: ", anotacoesGerais[0]['hora'])
            print("Dentista responsável: ", anotacoesGerais[0]['dentista'])
            print("Anotações: ", anotacoesGerais[0]['notas'])
        else:
            print("Não há anotações a serem mostradas no momento.")
    else: 
        print("Não há pacientes em atendimento no momento.")
        
#Função da opção 6 para ler a anotação da última vez que o paciente esteve na consulta
def lerUltimaAnotacao(nomePacienteAtendido):
    if nomePacienteAtendido != None:
        anotacoesGerais = listaDeAnotacoes(nomePacienteAtendido)
        quantidade = len(anotacoesGerais) - 1
        if anotacoesGerais != []:
            print("Paciente: ", nomePacienteAtendido)
            print("Alergias: ", anotacoesGerais[0]['alergia'])
            print("Motivo da consulta: ", anotacoesGerais[quantidade]['queixa'])
            print("Data do atendimento: ", anotacoesGerais[quantidade]['data'])
            print("Horário da sessão: ", anotacoesGerais[quantidade]['hora'])
            print("Dentista responsável: ", anotacoesGerais[quantidade]['dentista'])
            print("Anotações: ", anotacoesGerais[quantidade]['notas'])
        else:
            print("Não há anotações a serem mostradas no momento.")

    else: 
        print("Não há pacientes em atendimento no momento.")

#Função da opção 7 para anotar informações do paciente no prontuário
def anotarProntuario(nomePacienteAtendido, dentista):
    atendimento = 0

    if nomePacienteAtendido != None or nomePacienteAtendido != []:
        anotacoes = abrirArquivoLista('anotacoes.json')

        for dados in anotacoes:
            if nomePacienteAtendido == dados['paciente']:
                atendimento = 1

        dataHora = abrirArquivo("dataHoraSessaoAberta.json")
        if dataHora:
            data = dataHora['data']
            hora = dataHora['hora']

        if atendimento == 0:
            alergia = input("Alergias: ")
            queixa = input("Motivo da consulta: ")
            notas = input("Anotações: ")

            anotacoesAtuais = {
            'paciente': nomePacienteAtendido,
            'alergia': alergia,
            'queixa': queixa,
            'data': data,
            'hora': hora, 
            'dentista': dentista,
            'notas': notas,
            }

        elif atendimento == 1:
            queixa = input("Motivo da consulta: ")
            notas = input("Anotações: ")
        
            anotacoesAtuais = {
                'paciente': nomePacienteAtendido,
                'queixa': queixa,
                'data': data,
                'hora': hora,
                'dentista': dentista,
                'notas': notas
            }
        
        #Inserindo as anotações
        anotacoes.append(anotacoesAtuais)
        inserirDadosArquivo("anotacoes.json", anotacoes)
    else: 
        print("Não há pacientes em atendimento no momento.")
    
#Função para colocar as anotações do paciente que está sendo atendido dentro de uma lista
def listaDeAnotacoes(nomePacienteAtendido):
    anotacoesGerais = []
    listaAnotacoes = abrirArquivoLista("anotacoes.json")
    for dados in listaAnotacoes:
        if dados['paciente'] == nomePacienteAtendido:
            anotacoesGerais.append(dados)

    return anotacoesGerais

#Função para verificar se a sessão está aberta pelo dentista
def sessaoAbertaParaConsultas():
    sessaoConsultaAberta = abrirArquivo("dataHoraSessaoAberta.json")
    if sessaoConsultaAberta: 
        if sessaoConsultaAberta['sessaoAbertaConsulta'] == "Aberta":
            return True
        else:
            return False
    return False

#Função para verificar se a sessão está aberta após atender todos os pacientes, pois tendo vaga é possível que algum paciente apareça ainda para a consulta, sendo inserido na fila. 
def sessaoAbertaSemPacientesNaFila():
    sessaoConsultaAberta = abrirArquivo("dataHoraSessaoAberta.json")
    if sessaoConsultaAberta:
        if sessaoConsultaAberta['situacao'] == True:
            return True
        else:
            return False
    else:
        return False
