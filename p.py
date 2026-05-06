 # login
Usuario_ADM = [
["wallisson", "wallisson123@gmail.com", "#agronegócio"], ["guilherme", "guigui@gmail.com", "@algoritmos"], 
["renê", "gadelha@gmail.com", "coordenadoria26"], ["gilvan", "reigil@gmail.com", "gilvanII"]
]

Usuario_CLI = [
["gabriel", "gabrielbastos@gmail.com", "zecabode"], ["zacarias", "zacarias01@gmail.com", "fazendajatobar###"]
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
    print("----- Bem vindo ao Agro app -----")
    print("1 - login do usuario" )
    print("2 - cadastro de usuario")
    print("3 - Sair")
    op = int(input(""))
    if op == 1:
        nome = input("Nome: ")
        gmail = input("Email: ")
        senha = input("Senha: ")
    elif op == 2:
        nome = input("Nome: ")
        gmail = input("Email: ")
        senha = input("Senha: ")
        while True:
            
            if "@" in gmail and ".com" in gmail:
                print("Email válido")
            else:
                print("Email inválido! Deve conter @ e terminar com .com")
            if len(senha) >= 8:
                break
            else:
                print("Senha inválida! Mínimo 8 caracteres.")
            
            perfil = input("Perfil (adm/cliente): ")

            if perfil == "adm":
                Usuario_ADM.append([nome, gmail, senha])
                print("Usuário cadastrado com sucesso.")
                break  

            elif perfil == "cliente":
                Usuario_CLI.append([nome, gmail, senha])
                print("Usuário cadastrado com sucesso.")
                break 

            else:
                print("Inválido! Tente novamente.")

    elif op == 3:
        print("Saindo...")
        break
    else:
        print("Comando Inválido, tente novamente.")

# cliente
# admin
