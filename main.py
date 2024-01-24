"""Autor: Sayumi Mizogami Santana
Componente Curricular: EXA 854 - MI - Algoritmos
Concluído em: INFORME A DATA DE CONCLUSÃO
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação."""

from funcoes import *

encerrarPrograma = False
contadorSistema = 0

while encerrarPrograma != True:

    if contadorSistema == 0:
        usuario = login()
        print('\033c', end='')
    else: 
        resposta = input("Clique ENTER para continuar ")
        print('\033c', end='')
        usuario = login()

    contadorSistema += 1

    if usuario == "R":
        encerrarProgramaRecepcao = False
        cont = 0
        while encerrarProgramaRecepcao != True:
            if cont == 0:
                menuRecepcao()
            else: 
                resposta = input("Clique ENTER para continuar ")
                print('\033c', end='')
                menuRecepcao()

            cont += 1

            while True:
                try:
                    opcao = int(input("Opcão escolhida: "))
                except:
                    print("ERRO! Digite apenas números de 1 a 12!")
                else:
                    if 0 < opcao <= 12:
                        break
                    else:
                        print("ERRO! Digite apenas de 1 a 12!")
                        continue

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
                print("\nEncerrando...")
                encerrarProgramaRecepcao = True
            
            print("-"*47)

    elif usuario == "D":
        encerrarProgramaDentista = False
        atendendoPaciente = False
        cont = 0

        dentista = input("Insira o nome do dentista: ")

        while encerrarProgramaDentista != True:
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
                    anotarProntuario(nomePacienteAtendido, dentista)
                else:
                    print("ERRO!\nNão há pacientes sendo atendidos no momento!")

            elif opcao == 8:
                print("Encerrando...")
                encerrarProgramaDentista = True 

            print("-"*47)

    encerrar = input("Deseja encerrar o programa?[S/N]: ").upper()
    if encerrar == "S":
        encerrarPrograma = True


print("\n" + "*"*47 + "\n")
print("PROGRAMA ENCERRADO COM SUCESSO!".center(47))
print("\n" + "*"*47 + "\n")


            



