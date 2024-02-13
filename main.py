"""Autor: Sayumi Mizogami Santana
Componente Curricular: EXA 854 - MI - Algoritmos
Concluído em: 21/02/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação."""

#Sistema operacional utilizado: Windows

import funcoes
import os
encerrarPrograma = False
contadorSistema = 0

#O sistema continuará rodando até o encerrarPrograma seja True
while not encerrarPrograma:
    #Mostrando a tela de login pela primeira vez, para recepção ou dentista, sem necessitar da limpeza do terminal
    if contadorSistema == 0:
        usuario = funcoes.login()
        os.system('cls||clear')

    #Tela se limpa com a permissão do usuário para continuar utilizando o programa
    else: 
        resposta = input("Clique ENTER para continuar ")
        os.system('cls||clear')
        usuario = funcoes.login()
        os.system('cls||clear')

    contadorSistema += 1 #Contador para verificar se é a primeira vez que o programa está sendo rodado

    #Caso o usuário escolha a opção de recepção no login
    if usuario == 1:
        encerrarProgramaRecepcao = False
        cont = 0
        
        #Continuará rodando até o encerrarProgramaRecepcao seja False
        while not encerrarProgramaRecepcao:
            opcaoValida = False
            if cont == 0:
                funcoes.menuRecepcao()
            else: 
                resposta = input("Clique ENTER para continuar ")
                os.system('cls||clear')
                funcoes.menuRecepcao()

            cont += 1
            
            #Tratamento de dados inseridos pelo usuário
            while not opcaoValida:
                try:
                    opcao = int(input("Opcão escolhida: "))
                    if 0 < opcao <= 12:
                        opcaoValida = True
                    else:
                        print("ERRO! Digite apenas de 1 a 12!")
                except ValueError: 
                    print("ERRO! Digite apenas números de 1 a 12!")
                
            os.system('cls||clear')
            #Chamando as funções de acordo com e escolha do usuário no menu
            if opcao == 1:
                funcoes.cabecalho("ADICIONAR NOVA SESSÃO CLÍNICA")
                funcoes.adicionarNovaSessao()
                
            elif opcao == 2: 
                funcoes.cabecalho("LISTAR SESSÕES CLÍNICAS")
                funcoes.listarSessao()

            elif opcao == 3: 
                funcoes.cabecalho("BUSCAR SESSÕES CLÍNICAS")
                funcoes.buscarSessao()
            
            elif opcao == 4:
                funcoes.cabecalho("INICIAR SESSÃO")
                sessaoAberta = funcoes.sessaoAbertaOuFechada()
                
                #Verificação de sessão, caso já tenha uma sessão aberta, torna-se impossível iniciar uma nova ao mesmo tempo
                if sessaoAberta == False:
                    funcoes.iniciarSessao()
                else:
                    print("Há uma sessão aberta.\nTente novamente após encerrar a sessão atual.")
                
            elif opcao == 5:
                funcoes.cabecalho("CADASTRAR NOVO PACIENTE")
                funcoes.cadastrarPaciente()
                
            elif opcao == 6:
                funcoes.cabecalho("MARCAR HORÁRIO")
                funcoes.marcarHorario()
                
            elif opcao == 7:
                funcoes.cabecalho("LISTAR HORÁRIOS MARCADOS")
                funcoes.listarHorariosMarcados()

            elif opcao == 8:
                funcoes.cabecalho('VERIFICAR SE PACIENTE TEM HORÁRIO MARCADO')
                funcoes.confirmarHorario()
            
            elif opcao == 9: 
                funcoes.cabecalho("COLOCAR PACIENTE NA FILA")
                funcoes.colocarNaListaAtendimento()
            
            elif opcao == 10: 
                funcoes.cabecalho("PRÓXIMO PACIENTE")
                funcoes.listarProximos()

            elif opcao == 11:
                funcoes.cabecalho("CONSULTAS REALIZADAS NA SESSÃO")
                funcoes.listarConsultasRealizadas()
            
            elif opcao == 12:
                print("-"*47)
                print("Voltando para a página inicial...")
                encerrarProgramaRecepcao = True
                     
            print("-"*47)

    elif usuario == 2:
        encerrarProgramaDentista = False
        atendendoPaciente = False
        sessaoAbertaParaConsulta = False

        cont = 0
        print()
        #Solicitando o nome do dentista que está atendendo o paciente para que assim esteja o nome do profissional no prontuário do paciente.
        dentista = input("Insira o nome do dentista: ")
        os.system('cls||clear')

        #Enquando o usuário não optar por sair do sistema do dentista, o sistema rodará a tela do dentista
        while not encerrarProgramaDentista:
            opValida = False
            if cont == 0:
                funcoes.menuDentista()
            else: 
                resposta = input("Clique ENTER para continuar ")
                os.system('cls||clear')
                funcoes.menuDentista()

            cont += 1

            #Tratamento de dados, o usuário só poderá inserir números de 1 a 8
            while not opValida:
                try:
                    opcao = int(input("Opcão escolhida: "))

                    if 0 < opcao <= 8:
                        opValida = True
                    else:
                        print("ERRO! Digite apenas de 1 a 8!")
                except ValueError:
                    print("ERRO! Digite apenas números de 1 a 8!")

            os.system('cls||clear')
            #Chamando funções de acordo com a escolha do usuário
            if opcao == 1:
                funcoes.cabecalho("BUSCAR SESSÃO")
                funcoes.buscarSessao()

            elif opcao == 2:
                funcoes.cabecalho("INICIAR SESSÃO")
                funcoes.abrirSessaoConsulta()
                
            elif opcao == 3:
                funcoes.cabecalho("ATENDER PRÓXIMO PACIENTE")
                sessaoConsultaAberta = funcoes.sessaoAbertaParaConsultas()
                sessaoAbertaSemPaciente = funcoes.sessaoAbertaSemPacientesNaFila()
                print(sessaoConsultaAberta)
                if sessaoConsultaAberta:
                    nomePacienteAtendido = funcoes.atenderProxPaciente()
                    if sessaoAbertaSemPaciente:
                        atendendoPaciente = True #Para futuras verificações, caso não tenha nenhum paciente em atendimento muitos serviços serão impossibilitados de ocorrer
                
                else: 
                    print("ERRO! Não há sessões abertas para a consulta.\nTente novamente após iniciar a sessão para con-\nsulta na opção 2.")
                print(sessaoAbertaSemPaciente)
            elif opcao == 4: 
                funcoes.cabecalho("LER PRONTUÁRIO")
                if atendendoPaciente:  
                    funcoes.lerProntuario(nomePacienteAtendido)
                else:
                    print("ERRO!\nNão há pacientes sendo atendidos no momento!")

            elif opcao == 5: 
                funcoes.cabecalho("LER PRIMEIRA ANOTAÇÃO")
                if atendendoPaciente:
                    funcoes.lerPrimeiraAnotacao(nomePacienteAtendido)
                else:
                    print("ERRO!\nNão há pacientes sendo atendidos no momento!")

            elif opcao == 6: 
                funcoes.cabecalho("LER ÚLTIMA ANOTAÇÃO")
                print(atendendoPaciente)
                if atendendoPaciente:
                    funcoes.lerUltimaAnotacao(nomePacienteAtendido)
                else:
                    print("ERRO!\nNão há pacientes sendo atendidos no momento!")

            elif opcao == 7: 
                funcoes.cabecalho("ANOTAR NO PRONTUÁRIO")
                print(atendendoPaciente)
                if atendendoPaciente:
                    funcoes.anotarProntuario(nomePacienteAtendido, dentista)
                else:
                    print("ERRO!\nNão há pacientes sendo atendidos no momento!")

            elif opcao == 8:
                print("-"*47)
                print("Voltando para a página inicial...")
                encerrarProgramaDentista = True 

            print("-"*47)

    elif usuario == 3:
        encerrarPrograma = True

print("\n" + "*"*47 + "\n")
print("PROGRAMA ENCERRADO COM SUCESSO!".center(47))
print("\n" + "*"*47 + "\n")


            



