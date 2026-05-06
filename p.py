 # login
Usuario_ADM = [
["Wallisson", "Wallisson123@gmail.com", "#Agronegócio"], ["Guilherme", "GuiGui@gmail.com", "@Algoritmos"] 
["Renê", "Gadelha@gmail.com", "Coordenadoria26"], ["Gilvan", "ReiGil@gmail.com", "GilvanII!"]
]

Usuario_CLI = [
["Gabriel", "gabrielbastos@gmail.com", "zecabode"] ["Zacarias", "zacarias01@gmail.com", "fazendajatobar###"]
]

Usuarios = [Usuario_ADM, Usuario_CLI]

animais = ["Bovinos", "Ovinos", "Caprinos", "Aves", "Equinos", "Suinos"]
produtos = []
# qualquer coisa a gente add mais listas
id_produto = 1

#contador de produtos !
login_do_usuario = 0
perfil_do_login = 0

while True:
    print("-----Bem vindo Agro app -----")
    print("1 - login do usuario".lower )
    print("2 - login adm".lower)
    print("3 - cadastro do usuario".lower)
    print("4 - alterar produto".upper )
    print("5 - Sair")
    OP = int(input(""))

    if Usuario_CLI == "cli":
        print("---adm_logado---")
        print("1- cadastrar produto")
        #vamos colocar uma .apped para essa função
        print("2 - remover produto !")
        # vamos usar um .pop para essa função
        print("3 - adicionar animal")
        print("4 - remover animal")
        print("5 -  ")
        print("- sair")
    

    elif OP == 2:
        gmail = input("Email: ")
        senha = input("Senha: ")
        nome = input("Nome: ")
        perfil = input("Perfil (adm/cliente): ").lower
        Usuario_CLI.append([Usuario_CLI, gmail, senha])
        print("Usuário cadastrado com sucesso.")
    elif OP == 4:
        pid = int(input("ID para remover: "))
        for p in produtos:
            if p[0] == pid:
                produtos.pop(p)
                print("Removido com sucesso.")
                break

# cliente
# admin
    if Usuario_ADM == "adm":
        print("---adm_logado---")
        print("1- cadastrar produto")
        #vamos colocar uma .apped para essa função
        print("2 - remover produto !")
        # vamos usar um .pop para essa função
        print("3 - adicionar animal")
        print("4 - remover animal")
        print("5 -  ")
        print("- sair")
