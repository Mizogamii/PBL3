import json 

def escolhaUsuario():
    cabecalho("LOGIN")
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

def nomeDentista(text):
    print("_"*40)
    print()
    print(text.center(40))
    print("_"*40)

def cabecalho(texto):
    print("-"*40)
    print(texto.center(40))
    print("-"*40)


dictDados = {'Nome': 'Say', 'Idade': '22'}

for k, v in dictDados.items():
     print(k, v)

json.dumps(dictDados)

#Criando o arquivo em json
with open('dados.json', 'w') as arquivo:
     arquivo.write(json.dumps(dictDados))

with open('dados.json', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)


print(dados['Nome'])


nomeDentista("DENTECLEAN")

opcao = escolhaUsuario()
print(opcao)

if opcao == 1:
    cabecalho("RECEPÇÃO")
    login = str(input("Usuário: "))
    #Talvez nem precise disso de senha 
    senha = int(input("Senha: "))

elif opcao == 2:
    cabecalho("DENTISTA")
    login = str(input("Usuário: "))
    #Talvez nem precise disso de senha 
    senha = int(input("Senha: "))

#Determinando o que eu vou pedir de dados ao usuário!
"""
Do paciente:
Nome:
Data de nascimento --> se der quero fazer que nem em resultado de exame de médico que aparece que a pessoa tem X anos e Y meses de idade
Preferenci em dentista? --> acho que isso aqui só serve se a pessoa já tiver vindo mais de uma vez e também depois dos dentitas terem feito o cadastro deles
CPF: Só por pedir mesmo --> no caso se eu realmente pedir preciso tratar os dados inseridos 
Telefone: também preciso tratar
Endereço? Talvez seria interessante
Horário da sessão


Do dentista:
Nome: 
Código dele: Aí poderia ser selecionado o dentista pelo código
Que tipo de dentista? 

"""