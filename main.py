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
        iniciarSessao()
        
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



