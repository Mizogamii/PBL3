from funcoes import *

encerrarPrograma = False
cont = 0

    
while encerrarPrograma != True:
    if cont == 0:
        menuDentista()
    else: 
        resposta = input("Clique ENTER para continuar ")
        print('\033c', end='')
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
        atenderProxPaciente()

    elif opcao == 4: 
        cabecalho("LER PRONTUÁRIO")
        lerProntuario()

    elif opcao == 5: 
        cabecalho("LER PRIMEIRA ANOTAÇÃO")
        lerPrimeiraAnotacao()

    elif opcao == 6: 
        cabecalho("LER ÚLTIMA ANOTAÇÃO")
        lerUltimaAnotacao()

    elif opcao == 7: 
        cabecalho("ANOTAR NO PRONTUÁRIO")
        anotarProntuario()

    elif opcao == 8:
        print("Encerrando...")
        encerrarPrograma = True 

