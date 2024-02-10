from funcoes import *

encerrarPrograma = False
atendendoPaciente = False
cont = 0

while encerrarPrograma != True:
    if cont == 0:
        menuDentista()
    else: 
        resposta = input("Clique ENTER para continuar ")
        os.system('cls||clear')
        menuDentista()

    cont += 1

    while True:
        try:
            opcao = int(input("Opcão escolhida: "))
        except:
            print("ERRO! Digite apenas números de 1 a 8!")
        else:
            if 0 < opcao <= 8:
                break
            else:
                print("ERRO! Digite apenas de 1 a 8!")
                continue
    if opcao == 1:
        cabecalho("BUSCAR SESSÃO")
        buscarSessao()

    elif opcao == 2:
        cabecalho("INICIAR SESSÃO")
        sessaoAberta = sessaoAbertaOuFechada()
        
        if sessaoAberta == False:
            iniciarSessao()
        else:
            print("Há uma sessão aberta.\nTente novamente após encerrar a sessão atual.")

    elif opcao == 3:
        cabecalho("ATENDER PRÓXIMO PACIENTE")
        atendendoPaciente = True
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
            lerPrimeiraAnotacao(nomePacienteAtendido)
        else:
            print("ERRO!\nNão há pacientes sendo atendidos no momento!")

    elif opcao == 6: 
        cabecalho("LER ÚLTIMA ANOTAÇÃO")
        if atendendoPaciente == True:
            lerUltimaAnotacao(nomePacienteAtendido)
        else:
            print("ERRO!\nNão há pacientes sendo atendidos no momento!")

    elif opcao == 7: 
        cabecalho("ANOTAR NO PRONTUÁRIO")
        if atendendoPaciente == True:
            anotarProntuario(nomePacienteAtendido)
        else:
            print("ERRO!\nNão há pacientes sendo atendidos no momento!")

    elif opcao == 8:
        print("Encerrando...")
        encerrarPrograma = True 
        
    print("-"*47)
    
