def escolhaUsuario():
    print("-"*40)
    print("                 LOGIN                  ")
    print("-"*40)
    print("Para recepção digite 1\nPara dentista digite 2")
    print("-"*40)
    while True:
            try:        
                usuario = int(input("Opção:"))
                if usuario != 1 and usuario != 2:
                    print("Digite apenas números 1 ou 2!")
                    continue
                return usuario
            except:
                print("ERRO! Digite apenas números!")
                
opcao = escolhaUsuario()
print(opcao)
if opcao == 1:
     print("")