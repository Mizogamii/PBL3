"""Autor: Sayumi Mizogami Santana
Componente Curricular: EXA 854 - MI - Algoritmos
Concluído em: 21/02/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação."""

#Sistema operacional utilizado: Windows

from funcoes import *
import os
encerrarPrograma = False
contadorSistema = 0

#O sistema continuará rodando até o encerrarPrograma seja True
while not encerrarPrograma:
    #Mostrando a tela de login pela primeira vez, para recepção ou dentista, sem necessitar da limpeza do terminal
    if contadorSistema == 0:
        usuario = login()
        os.system('cls||clear')

    #Tela se limpa com a permissão do usuário para continuar utilizando o programa
    else: 
        resposta = input("Clique ENTER para continuar ")
        os.system('cls||clear')
        usuario = login()
        os.system('cls||clear')

    contadorSistema += 1 #Contador para verificar se é a primeira vez que o programa está sendo rodado

    #Caso o usuário escolha a opção de recepção no login
    if usuario == 1:
        encerrarProgramaRecepcao = False
        cont = 0
        opcaoValida = False
        
        #Continuará rodando até o encerrarProgramaRecepcao seja False
        while not encerrarProgramaRecepcao:
            if cont == 0:
                menuRecepcao()
            else: 
                resposta = input("Clique ENTER para continuar ")
                os.system('cls||clear')
                menuRecepcao()

            cont += 1

            #Tratamento de dados inseridos pelo usuário
            while not opcaoValida:
                try:
                    opcao = int(input("Opcão escolhida: "))
                    if 0 < opcao <= 12:
                        opcaoValida = True
                    else:
                        print("ERRO! Digite apenas de 1 a 12!")
                except:
                    print("ERRO! Digite apenas números de 1 a 12!")

            #Chamando as funções de acordo com e escolha do usuário no menu
            if opcao == 1:
                cabecalho("ADICIONAR NOVA SESSÃO CLÍNICA")
                adicionarNovaSessao()
                
            elif opcao == 2: 
                cabecalho("LISTAR SESSÕES CLÍNICAS")
                listarSessao()

            elif opcao == 3: 
                cabecalho("BUSCAR SESSÕES CLÍNICAS")
                buscarSessao()
            
            elif opcao == 4:
                cabecalho("INICIAR SESSÃO")
                sessaoAberta = sessaoAbertaOuFechada()
                
                #Verificação de sessão, caso já tenha uma sessão aberta, torna-se impossível iniciar uma nova ao mesmo tempo
                if sessaoAberta == False:
                    iniciarSessao()
                else:
                    print("Há uma sessão aberta.\nTente novamente após encerrar a sessão atual.")
                
            elif opcao == 5:
                cabecalho("CADASTRAR NOVO PACIENTE")
                cadastrarPaciente()
                
            elif opcao == 6:
                cabecalho("MARCAR HORÁRIO")
                marcarHorario()
                
            elif opcao == 7:
                cabecalho("LISTAR HORÁRIOS MARCADOS")
                listarHorariosMarcados()

            elif opcao == 8:
                cabecalho('VERIFICAR SE PACIENTE TEM HORÁRIO MARCADO')
                confirmarHorario()
            
            elif opcao == 9: 
                cabecalho("COLOCAR PACIENTE NA FILA")
                colocarNaListaAtendimento()
            
            elif opcao == 10: 
                cabecalho("PRÓXIMO PACIENTE")
                listarProximos()

            elif opcao == 11:
                cabecalho("CONSULTAS REALIZADAS NA SESSÃO")
                listarConsultasRealizadas()
            
            elif opcao == 12:
                encerrarProgramaRecepcao = True
            
            print("-"*47)

    elif usuario == 2:
        encerrarProgramaDentista = False
        atendendoPaciente = False
        cont = 0
        print("."*47)
        #Solicitando o nome do dentista que está atendendo o paciente para que assim esteja o nome do profissional no prontuário do paciente.
        dentista = input("Insira o nome do dentista: ")
        print("."*47)

        #Enquando o usuário não optar por sair do sistema do dentista, o sistema rodará a tela do dentista
        while not encerrarProgramaDentista:
            opValida = False
            if cont == 0:
                menuDentista()
            else: 
                resposta = input("Clique ENTER para continuar ")
                os.system('cls||clear')
                menuDentista()

            cont += 1

            #Tratamento de dados, o usuário só poderá inserir números de 1 a 8
            while not opValida:
                try:
                    opcao = int(input("Opcão escolhida: "))

                    if 0 < opcao <= 8:
                        opValida = True
                    else:
                        print("ERRO! Digite apenas de 1 a 8!")
                except:
                    print("ERRO! Digite apenas números de 1 a 8!")

            #Chamando funções de acordo com a escolha do usuário
            if opcao == 1:
                cabecalho("BUSCAR SESSÃO")
                buscarSessao()

            elif opcao == 2:
                cabecalho("INICIAR SESSÃO")
                sessaoAbertaParaConsulta = abrirSessaoConsulta()
                

            elif opcao == 3:
                cabecalho("ATENDER PRÓXIMO PACIENTE")
                atendendoPaciente = True #Para futuras verificações, caso não tenha nenhum paciente em atendimento muitos serviços serão impossibilitados de ocorrer
                nomePacienteAtendido = atenderProxPaciente()

            elif opcao == 4: 
                cabecalho("LER PRONTUÁRIO")
                if atendendoPaciente == True:  
                    lerProntuario(nomePacienteAtendido)
                else:
                    print("ERRO!\nNão há pacientes sendo atendidos no momento!")

            elif opcao == 5: 
                cabecalho("LER PRIMEIRA ANOTAÇÃO")
                if atendendoPaciente == True:
                    lerPrimeiraAnotacao(nomePacienteAtendido, dentista)
                else:
                    print("ERRO!\nNão há pacientes sendo atendidos no momento!")

            elif opcao == 6: 
                cabecalho("LER ÚLTIMA ANOTAÇÃO")
                if atendendoPaciente == True:
                    lerUltimaAnotacao(nomePacienteAtendido, dentista)
                else:
                    print("ERRO!\nNão há pacientes sendo atendidos no momento!")

            elif opcao == 7: 
                cabecalho("ANOTAR NO PRONTUÁRIO")
                if atendendoPaciente == True:
                    anotarProntuario(nomePacienteAtendido, dentista)
                else:
                    print("ERRO!\nNão há pacientes sendo atendidos no momento!")

            elif opcao == 8:
                print("Encerrando...")
                encerrarProgramaDentista = True 

            print("-"*47)

    elif usuario == 3:
        encerrarPrograma = True

print("\n" + "*"*47 + "\n")
print("PROGRAMA ENCERRADO COM SUCESSO!".center(47))
print("\n" + "*"*47 + "\n")


            



