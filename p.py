 # login
Usuarios = 

Usuario_ADM = [
["Wallisson", "#Agronegócio"], ["Guilherme", "@Algoritmos"] 
["Renê", "Coordenadoria26"], ["Gilvan", "GilvanII!"]
]

Usuario_CLI = [
["Gabriel", "zecabode"]
]
animais = ["Bovinos", "Ovinos", "Caprinos", "Aves", "Equinos", "Suinos"]
produtos = []
# qualquer coisa a gente add mais listas
id_produto = 1
#contador de produtos !
login_do_usuario = 0
perfil-do-login = 0

while True:
    print("-----Bem vindo Agroapp -----")
    print("1 - login do usuario")
    print("2 - login adm")
    print("3 - cadastro do usuario")
    print("4 - alterar produto" )
    print("5 - Sair")
    OP = int(input(""))

    if Login == "adm":
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
        login = input("Email: ")
        senha = input("Senha: ")
        nome = input("Nome: ")
        perfil = input("Perfil (adm/cliente): ").lower
        usuarios.append([login, senha, perfil, nome])
        print("Usuário cadastrado com sucesso.")
    elif op == 4:
        pid = int(input("ID para remover: "))
        for p in produtos:
            if p[0] == pid:
                produtos.pop(p)
                print("Removido com sucesso.")
                break

# cliente
# admin
