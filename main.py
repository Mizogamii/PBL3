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
cont = 0

while encerrarPrograma != True:
    if cont == 0:
        menu()
    else: 
        resposta = input("Clique ENTER para continuar ")
        print('\033c', end='')
        menu()

    cont += 1

    while True:
        try:
            opcao = int(input("Opcão escolhida: "))
        except:
            print("ERRO! Digite apenas números de 1 a 10!")
        else:
            if 0 < opcao <= 10:
                break
            else:
                print("ERRO! Digite apenas de 1 a 10!")
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
        iniciarSessao()
        
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
    
    elif opcao == 9: 
        cabecalho("LISTAR PRÓXIMOS PACIENTES")

    elif opcao == 10:
        print("\nEncerrando...")
        encerrarPrograma = True
    
    print("-"*47)



